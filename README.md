# System Health Monitor

## Description

This script constantly monitors the health of specific system components (printer, internet connection, CPU, and memory) on a Windows machine. When it detects issues, such as the printer being out of paper or a high CPU usage, it sends an email notification to a predefined email address.

## Features

- **Printer Health Check**: Monitors the health status of two specified printers and notifies about any error states like paper jam, no toner, offline, etc.
- **Internet Connection Check**: Pings Google's public DNS server to ensure the machine has active internet connectivity.
- **System Resource Monitor**: Monitors CPU and Memory usage; if either surpasses 80%, an email is sent.
- **Email Notification**: Sends an email when an error is detected in any of the monitored components.
- **Startup Integration**: Provides a method to add this script to Windows startup.

## Prerequisites

- Python environment (preferably Python 3.x).
- Required Python packages:
  - `win32print`
  - `socket`
  - `psutil`
  - `yagmail`
  - `smtplib`
  - `platform`
  - `datetime`
  - `getpass`
  - `os`
  - `subprocess`

## Setup

1. Install the required Python packages:

   ```
   pip install win32print psutil yagmail
   ```

2. Update the global variables in the script:

   - Set your printers' names in `printer_name` and `printer_name_1`.
   - Update the `LOGIN_EMAIL_SEND_FROM`, `LOGIN_EMAIL_SEND_TO`, and `LOGIN_PASSWORD` with your desired email credentials.

## Usage

1. Run the script:

   ```
   python monitor.pyw
   ```

2. The script will start its monitoring loop, checking each component in intervals of 180 seconds (3 minutes) by default. Adjust the `time.sleep(180)` for a different interval.

3. In case you want to add this script to start with Windows, uncomment the line `#add_to_startup()` in the `main()` function.

## Notes

1. FTP login credentials have been hardcoded for demonstration purposes. In a production environment, consider using environment variables or secure vaults to store sensitive information.
2. The script sends an email for each error detected in the interval, which might lead to multiple emails if not resolved.
3. Ensure your email service provider allows SMTP access for sending emails through scripts. Some providers might block it due to security concerns.
4. Make sure you have the required permissions to add scripts to Windows startup.

## File Type Information

This script is saved with a `.pyw` extension, which means it's a Python script for Windows that runs without launching a command prompt window. Unlike the usual `.py` files which open a terminal window when executed, `.pyw` scripts run silently in the background. Ensure that you use the appropriate Python interpreter to execute this script, or simply double-click the `.pyw` file to run it (given that you have Python installed on your system).

## Contributing

If you have suggestions for improvements or bug fixes, please consider creating pull requests or reporting the issues.

## License

Please ensure appropriate licensing for your project, especially if you are distributing or using it in a commercial environment.
