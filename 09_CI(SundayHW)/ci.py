import subprocess
import sys


def run_command(command):
    """Execute a shell command and print the output."""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}", file=sys.stderr)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)


def check_code_quality():
    """Run flake8 to check code formatting and indentation."""
    print("\n🔹 Checking code formatting with flake8...")
    run_command("flake8 --max-line-length=100 .")


def run_tests():
    """Run pytest to execute all test cases."""
    print("\n🔹 Running test cases with pytest...")
    run_command("pytest --maxfail=1 --disable-warnings -q")


if __name__ == "__main__":
    print("🚀 Starting CI checks...\n")
    check_code_quality()
    run_tests()
    print("\n✅ CI checks completed successfully!")