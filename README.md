# Website Health Checker
==========================

## Overview

This script checks the health of specified websites, including their status, speed, SEO details, and domain expiry. It can be configured to run periodically using Windows Task Scheduler.

## Dependencies

1. **Python 3.x**: Ensure Python 3 is installed on your system.
2. **Required Python Packages**: Install the necessary Python packages using `pip`.

   ```bash
   pip install requests whois python-dotenv
   ```

## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/your-repository/website-health-checker.git
cd website-health-checker
```
2. Create a .env in your root directory
```bash
# .env
URLS="https:/example.com,
https://salim.vercel.app"
CHECK_INTERVAL_HOURS=4
```
 **URLS**: Comma-separated list of URLs to check.
 
 **CHECK_INTERVAL_HOURS**: Interval in hours for how often the script should run.

## Configure Task Scheduler

### Open Task Scheduler

Press `Win + S`, type "Task Scheduler," and press `Enter`.

### Create a New Task

#### General Tab

* **Name:** "Website Health Checker"
* **Description:** "Runs the health checker script"
* **Security options:** "Run whether the user is logged on or not"
* **Run with highest privileges:** Check this box.

#### Triggers Tab

* Click "New..."
* **Begin the task:** "At startup"
* Click "OK".

#### Actions Tab

* Click "New..."
* **Action:** "Start a program"
* **Program/script:** `C:\Python39\python.exe` (update the path to your Python executable)
* **Add arguments:** `C:\path\to\website-health-checker\main.py` (update the path to your script)
* **Start in:** `C:\path\to\website-health-checker` (update to your script’s directory)
* Click "OK".

#### Conditions Tab (Optional)

Configure as needed.

#### Settings Tab

* **Allow task to be run on demand:** Check this box.
* **Run task as soon as possible after a scheduled start is missed:** Check this box.
* **If the task fails, restart every:** Set to your preference (e.g., 5 minutes, up to 3 times).
* Click "OK" to save the task.

### Running the Script

To test the script manually, run:
```bash
python main.py
