#This is LogHawk - A monitoring tool for security professionals by Lindsey Henderson.

import re
import os
import time
import logging
from datetime import datetime
import configparser
import subprocess

# Step 1: Configure Logging
logging.basicConfig(
    filename='/tmp/loghawk.log',  # Log file where alerts will be stored
    level=logging.INFO,  # Log level to store info and alerts
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format of log messages
)

# Step 2: Read and parse the config file for custom search rules
def load_config(config_path='config.ini'):
    """Load search patterns and thresholds from config file."""
    config = configparser.ConfigParser()
    config.read(config_path)
    
    # If config file doesn't exist, we set defaults
    if not config.read(config_path):
        logging.warning("Config file not found, using default patterns.")
    
    search_rules = {
        'failed_logins': config.get('Patterns', 'failed_logins', fallback=r'Failed password'),
        'unauthorized_access': config.get('Patterns', 'unauthorized_access', fallback=r'401 Unauthorized'),
        'critical_errors': config.get('Patterns', 'critical_errors', fallback=r'(ERROR|CRITICAL)'),
        'bot_traffic': config.get('Patterns', 'bot_traffic', fallback=r'(bot|crawl|scanner)')
    }
    return search_rules

# Step 3: Function to scan logs using patterns (regex)
def scan_log_file(log_file, search_patterns):
    """Scan the given log file and check for patterns."""
    found_matches = []
    
    with open(log_file, 'r') as file:
        for line in file:
            for pattern_name, pattern in search_patterns.items():
                # Search for pattern matches in each line of the log file
                if re.search(pattern, line):
                    found_matches.append((pattern_name, line.strip()))
    
    return found_matches

# Step 4: Function to generate alerts based on findings
def generate_alerts(matches):
    """Generate alerts for suspicious activity."""
    for pattern_name, line in matches:
        # Generating alerts for matching patterns
        if pattern_name == 'failed_logins':
            alert_message = f"Alert: Too many failed logins detected - {line}"
            logging.warning(alert_message)  # Log as a warning
        elif pattern_name == 'unauthorized_access':
            alert_message = f"Alert: Unauthorized access attempt - {line}"
            logging.error(alert_message)  # Log as an error
        elif pattern_name == 'critical_errors':
            alert_message = f"Critical system error detected - {line}"
            logging.critical(alert_message)  # Log as critical
        elif pattern_name == 'bot_traffic':
            alert_message = f"Suspicious bot traffic detected - {line}"
            logging.info(alert_message)  # Log as info for tracking bots
            
        print(alert_message)  # Print the alert on screen for immediate attention

# Step 5: Automatically run the script using Cron (simulating it here by timing)
def schedule_log_scan(log_file, search_patterns, interval=600):
    """Automatically run the scan every 'interval' seconds (default: every 10 minutes)."""
    print(f"Scheduling log scan every {interval} seconds...")
    while True:
        print(f"Running log scan at {datetime.now()}")
        matches = scan_log_file(log_file, search_patterns)
        if matches:
            generate_alerts(matches)  # Generate alerts if suspicious activity found
        time.sleep(interval)  # Wait for the next scan

# Main function to execute the program
def main():
    """Main function to run the LogHawk monitoring tool."""
    
    # Step 1: Load search patterns from config file
    search_patterns = load_config()
    
    # Step 2: Set the log file to monitor (assume apache access log for this example)
    log_file = '/var/log/apache2/access.log'  # Replace with your actual log file path
    
    # Step 3: Simulate cron job by calling the function to scan logs every 10 minutes
    schedule_log_scan(log_file, search_patterns)

if __name__ == '__main__':
    main()
