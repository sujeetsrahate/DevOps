import psutil
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Email Configuration
SMTP_SERVER = "smtp.example.com"  # Change this to your SMTP server
SMTP_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECIPIENT = "recipient@example.com"

# CPU Threshold
CPU_THRESHOLD = 60

def send_email(subject, body):
    """Send an email alert."""
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USERNAME
    msg["To"] = EMAIL_RECIPIENT
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, EMAIL_RECIPIENT, msg.as_string())
        server.quit()
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def is_system_process(proc):
    """Check if a process belongs to the system."""
    try:
        username = proc.username()
        return username in ("root", "SYSTEM", "NT AUTHORITY\\SYSTEM")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def is_stress_process(proc):
    """Check if a process is from the stress utility."""
    try:
        return "stress" in proc.name().lower()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return False

def monitor_cpu():
    """Monitor CPU usage and take action if threshold is exceeded."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=2)
        if cpu_usage > CPU_THRESHOLD:
            print(f"High CPU Usage Detected: {cpu_usage}%")
            
            # Get process using the most CPU
            top_process = max(psutil.process_iter(attrs=['pid', 'name', 'cpu_percent', 'username']), 
                              key=lambda p: p.info['cpu_percent'])

            pid = top_process.info['pid']
            name = top_process.info['name']
            cpu_percent = top_process.info['cpu_percent']

            print(f"Top Process: {name} (PID: {pid}) - {cpu_percent}% CPU")

            if is_system_process(top_process):
                send_email("High CPU Alert", f"System Process {name} (PID: {pid}) is consuming {cpu_percent}% CPU.")
            elif is_stress_process(top_process):
                print(f"Stress utility detected: {name} (PID: {pid}) using {cpu_percent}% CPU")
            else:
                print(f"Killing Application Process: {name} (PID: {pid})")
                try:
                    psutil.Process(pid).terminate()
                    print(f"Process {name} (PID: {pid}) terminated.")
                except Exception as e:
                    print(f"Failed to terminate process: {e}")

        time.sleep(5)  # Monitor every 5 seconds

if __name__ == "__main__":
    monitor_cpu()
