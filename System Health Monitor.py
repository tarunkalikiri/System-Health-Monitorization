import psutil
import logging
from datetime import datetime

CPU_THRESHOLD = 80.0 
MEMORY_THRESHOLD = 80.0  
DISK_THRESHOLD = 80.0  
PROCESS_THRESHOLD = 200 
LOG_FILE = "system_health.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_alert(message):
    print(message)
    logging.warning(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        log_alert(f"High number of running processes detected: {processes}")
    return processes

def monitor_system():
    print("Starting system health monitoring...")
    logging.info("System health monitoring started.")

    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_usage()
    processes = check_running_processes()

    print("System Health Summary:")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")

if __name__ == "__main__":
    monitor_system()
