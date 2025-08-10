This script demonstrates how to automate Git commits using a Python script.  
You can use **Windows Task Scheduler** or **Linux/macOS cron** to run it at the OS level. 

> Note: The automation will only work if your computer is turned on at the scheduled time.

# Windows

Use Task Scheduler to create a new task:

<img width="472" height="291" alt="image" src="https://github.com/user-attachments/assets/55446166-cfb6-4924-8856-7d8f3e89ae98" />

<img width="1560" height="863" alt="Screenshot 2025-08-10 104216" src="https://github.com/user-attachments/assets/283e936c-5584-40e8-a1a6-a6d2dea962e0" />

- Set the trigger to run daily at your preferred time.
- Set the action to run `python` (or `python3`) with the full path to this script.
- (Optional) Enable **"Wake the computer to run this task"** if you use sleep mode.
- (Optional) Enable **"Run task as soon as possible after a scheduled start is missed"** so it runs after boot if the PC was off.

# Linux/macOS
Example cron job to run the script every day at 9 AM:  

```sh
0 9 * * * /usr/bin/python3 /path/to/your/main.py
```
