import os
import time
import signal
import sys
import re
from collections import Counter

log_dir = "logs"
log_file_name = "log_file.log"
log_file_path = os.path.join(log_dir, log_file_name)

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

keywords = {
    "error": {"severity": "Critical", "urgency": "High"},
    "warning": {"severity": "Warning", "urgency": "Medium"},
    "info": {"severity": "Informational", "urgency": "Low"},
    "HTTP": {"severity": "Informational", "urgency": "Low"}
}

def signal_handler(sig, frame):
    print("\nStopping log generation...")
    generate_summary_report()
    print("Exiting...")
    sys.exit(0)

def monitor_log_file(log_file_path):
    try:
        with open(log_file_path, "r") as file:
            file.seek(0, 2)
            while True:
                new_line = file.readline()
                if new_line:
                    print(new_line.strip())
                    analyze_log_entry(new_line.strip())
                time.sleep(0.1)
    except FileNotFoundError:
        print(f"Log file not found: {log_file_path}")
        sys.exit(1)

def analyze_log_entry(log_entry):
    for keyword, properties in keywords.items():
        count = len(re.findall(r'\b{}\b'.format(re.escape(keyword)), log_entry, flags=re.IGNORECASE))
        if count > 0:
            print(f"Count of '{keyword}' in log entry: {count}")
            print(f"Severity: {properties['severity']}, Urgency: {properties['urgency']}")

def generate_summary_report():
    with open(log_file_path, "r") as file:
        log_entries = file.readlines()
    
    keyword_counts = Counter()
    for keyword in keywords.keys():
        keyword_counts[keyword] = sum(1 for entry in log_entries if re.search(r'\b{}\b'.format(re.escape(keyword)), entry, flags=re.IGNORECASE))
    
    print("\nSummary Report for the entire log:")
    for keyword, count in keyword_counts.items():
        severity = keywords[keyword]["severity"]
        urgency = keywords[keyword]["urgency"]
        print(f"Count of '{keyword}' - Severity: {severity}, Urgency: {urgency}: {count}")

signal.signal(signal.SIGINT, signal_handler)

print(f"Monitoring log file: {log_file_path}")
try:
    monitor_log_file(log_file_path)
except KeyboardInterrupt:
    generate_summary_report()
    print("Exiting...")
