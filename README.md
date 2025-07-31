# LogHawk

LogHawk is a simple, open-source log monitoring and analysis tool designed to help security teams automatically detect and analyze suspicious activity in log files. The tool can identify security threats such as failed login attempts, unauthorized access, critical errors, unusual traffic spikes, and suspicious script activities.

## Disclaimer

LogHawk is an open-source project intended for educational and testing purposes. It is not guaranteed to catch all security threats or work in all environments. Use it at your own risk, and remember to perform comprehensive testing before deploying it in a production environment.


## Why Security Teams Need LogHawk

LogHawk provides a fast, automated way to monitor and filter logs for potential threats. By scanning logs for key patterns and behaviors that indicate potential issues, LogHawk helps security analysts detect threats early and respond proactively. This tool is designed to be lightweight, easy to use, and flexible, so teams can customize it for their own security monitoring needs.

## Features

- **Failed Login Detection**: Identifies repeated failed login attempts, which may indicate a brute-force attack.
- **Traffic Monitoring**: Detects unusual traffic patterns or spikes that could indicate a bot or vulnerability scanner.
- **Critical Error Alerts**: Identifies critical system errors or issues by scanning for ERROR or CRITICAL messages in logs.
- **Suspicious Script Activity**: Alerts you to unexpected cron jobs or unauthorized script executions.
- **Customizable Rules**: Users can define their own custom search rules for log scanning.

## Installation

To get started with LogHawk, follow these steps:

1. **Clone this repository** to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/loghawk.git

2. **Install Python 3** (if not already installed):
   ```bash
   sudo apt-get install python3

3. **Run LogHawk**:
  To use LogHawk, simply run the Python script with the path to the log file you want to scan:
   ```bash
   python3 loghawk.py /path/to/logfile.log

## Limitations

LogHawk is designed for quick detection of common patterns in log files, but it may not catch all sophisticated attacks or threats. Always complement LogHawk with other security tools and analysis methods for comprehensive monitoring.

## Customizing Your LogHawk

LogHawk allows users to define custom search rules by editing the config.json file. This makes it easy to tailor the log analysis to match specific security needs.

Example config.json:
```json
{
  "failed_logins": {
    "enabled": true,
    "threshold": 5,
    "logfile": "/var/log/auth.log"
  },
  "error_detection": {
    "enabled": true,
    "keywords": ["ERROR", "CRITICAL"]
  }
}
```

## License

LogHawk is released under the MIT License. Feel free to use, modify, and share it. However, remember that LogHawk is an open-source tool, so use it responsibly. We are not liable for any damage caused by misuse or misconfigurations.

## Contributing
LogHawk is open-source and contributions are welcome! If you find a bug, have a feature request, or want to improve the tool, feel free to submit a pull request or open an issue.

To contribute:

- Fork the repository.

- Create a new branch.

- Make your changes and commit them.

- Push to your fork and create a pull request.

## Example Output
```bash
[ALERT] Failed login attempts from IP 192.168.0.1 detected in /var/log/auth.log
[INFO] Loghawk detected 3 unusual traffic spikes from IP 10.0.0.5 in /var/log/apache2/access.log
````

## How to Automate with Cron
To automate LogHawk and run it every 10 minutes, set up a cron job. Open your crontab with:
```bash
crontab -e
```
Add the following line to run LogHawk every 10 minutes:
```bash
*/10 * * * * /usr/bin/python3 /path/to/loghawk.py /path/to/logfile.log
```

## References
- **Python Logging Documentation:** https://docs.python.org/3/library/logging.html
- **Cron Job Syntax:** https://man7.org/linux/man-pages/man5/crontab.5.html

