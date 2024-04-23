import os
import time
import random


log_dir = "logs"
log_file_name = "log_file.log"
log_file_path = os.path.join(log_dir, log_file_name)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_messages = [
    "INFO: This is an informational message.",
    "ERROR: An error occurred.",
    "DEBUG: Debugging information.",
    "WARNING: This is a warning message.",
    "CRITICAL: A critical error occurred."
]

http_status_codes = [
    "200 OK",
    "404 Not Found",
    "500 Internal Server Error",
    "302 Found",
    "401 Unauthorized"
]

def generate_log():
    while True:
        with open(log_file_path, "a") as file:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            log_level = random.choice(["INFO", "ERROR", "DEBUG", "WARNING", "CRITICAL"])
            log_message = random.choice(log_messages)
            http_status = random.choice(http_status_codes)
            log_entry = f"[{timestamp}] {log_level}: {log_message} - HTTP Status: {http_status}\n"
            file.write(log_entry)
        time.sleep(random.uniform(0.1, 2.0))

print(f"Generating logs to: {log_file_path}")
try:
    generate_log()
except KeyboardInterrupt:
    print("\nLog generation stopped.")
