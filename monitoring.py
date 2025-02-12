import psutil
import time

# Predefined threshold for CPU usage
threshold = 40

def monitor_cpu_usage():
    try:
        while True:
            # Get the current CPU usage
            cpu_usage = psutil.cpu_percent(interval=1)

            # Check if CPU usage exceeds the threshold
            if cpu_usage > threshold:
                print(f"Alert: CPU usage is {cpu_usage}%!")

            # Wait for a second before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        print("Monitoring stopped.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Start monitoring CPU usage
print("Monitoring CPU usage...")
monitor_cpu_usage()