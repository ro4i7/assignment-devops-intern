### Log Analysis and Monitoring Script

#### Introduction:
This project consists of two Python scripts, `generate_log.py` for generating log entries and `logm.py` for monitoring and analyzing log files. The `generate_log.py` script simulates log entries of various levels (INFO, ERROR, DEBUG, WARNING, CRITICAL) and HTTP status codes, while `logm.py` monitors the log file in real-time, analyzes the log entries, and generates summary reports.

#### Prerequisites:
- Python 3.x
- Operating System: Linux or macOS (for signal handling)

#### Dependencies:
- None

## Steps to Run the Scripts:

1. Clone or download the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Open the project folder in Visual Studio Code (VSCode).
4. Open the terminal window.
   
**5. Generating Logs:**
- Run the `generate_log.py` script using the following command:
```bash 
   python generate_log.py
```
This script continuously generates log entries and saves them to the `logs/log_file.log` file.

**6. Monitoring and Analyzing Logs:**
- Simultaneously Open a new terminal window or tab.
- Run the `logm.py` script using the following command:
```bash 
   python logm.py
```
This script monitors the log file in real time, analyzes the log entries for specific keywords, and generates summary reports.

**7. For Summary Reports:**

#### Stop the Scripts:
- First, stop the generation script (`generate_log.py`), press `Ctrl+C` in the terminal window where the script is running.
- Second, stop the log monitoring and analysis script (`logm.py`), press `Ctrl+C` in the terminal window where the script is running.

## After, just stopping the script, the Summary of reports will be displayed in the terminal window where the `logm.py` script is running.

#### Note:
- The log files will be saved in the `logs` directory relative to the location of the scripts.

