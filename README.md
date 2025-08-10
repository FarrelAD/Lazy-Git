This script demonstrates how to automate Git commits using a Python script.  
You can use **Windows Task Scheduler** or **Linux/macOS cron** to run it at the OS level. 

> Note: The automation will only work if your computer is turned on at the scheduled time.

# Windows
Use Task Scheduler to create a new task:
- Set the trigger to run daily at your preferred time.
- Set the action to run `python` (or `python3`) with the full path to this script.
- (Optional) Enable **"Wake the computer to run this task"** if you use sleep mode.
- (Optional) Enable **"Run task as soon as possible after a scheduled start is missed"** so it runs after boot if the PC was off.

# Linux/macOS
Example cron job to run the script every day at 9 AM:  

```sh
0 9 * * * /usr/bin/python3 /path/to/your/main.py
```