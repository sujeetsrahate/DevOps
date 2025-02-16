#!/bin/bash

# Define system processes (Modify according to your system)
SYSTEM_PROCESSES=("systemd" "init" "kthreadd" "ksoftirqd" "kswapd" "bioset" "udevd" "dbus-daemon")

# Email Configuration (Replace with your credentials)
SENDER_EMAIL="sujeetrahate@gmail.com"
RECEIVER_EMAIL="sujeetrahate@gmail.com"
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
EMAIL_PASSWORD="ohzi uzyc wkup wjey"  # ⚠ Use an App Password, NOT your actual password

# Function to send email alerts
send_email() {
    local subject="$1"
    local body="$2"
    
    echo -e "Subject: $subject\n\n$body" | sendmail -v -f "$SENDER_EMAIL" "$RECEIVER_EMAIL"
}

# Function to restart a process
restart_process() {
    local process_name="$1"
    echo "Restarting process: $process_name"
    pkill -f "$process_name"
    sleep 2
    nohup "$process_name" &>/dev/null &
}

# Function to kill unwanted processes
kill_process() {
    local process_name="$1"
    echo "Killing process: $process_name"
    pkill -f "$process_name"
}

# Function to monitor CPU usage
monitor_cpu() {
    while true; do
        CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')  # Get total CPU usage
        echo "CPU Utilization: $CPU_USAGE%"

        if (( $(echo "$CPU_USAGE > 10" | bc -l) )); then  # If CPU usage > 10%
            # Get high-CPU usage processes (above 60%)
            ps -eo pid,comm,%cpu --sort=-%cpu | awk '$3 > 60 {print $1, $2, $3}' | while read -r pid process_name cpu_usage; do
                echo "Process: $process_name, PID: $pid, CPU Usage: $cpu_usage%"

                # Check if the process is a system process
                if [[ " ${SYSTEM_PROCESSES[@]} " =~ " ${process_name} " ]]; then
                    send_email "High CPU Alert: $process_name" "The system process $process_name is using $cpu_usage% CPU."
                elif [[ "$process_name" != "bash" && "$process_name" != "monitor_cpu.sh" ]]; then
                    restart_process "$process_name"
                    send_email "High CPU Alert: $process_name" "The application process $process_name was restarted due to high CPU usage ($cpu_usage%)."
                else
                    kill_process "$process_name"
                    send_email "High CPU Alert: $process_name" "The process $process_name was killed due to excessive CPU usage ($cpu_usage%)."
                fi
            done
        fi

        sleep 5  # Wait for 5 seconds before checking again
    done
}

# Run the CPU monitor
monitor_cpu
