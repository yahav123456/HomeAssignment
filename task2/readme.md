# CPU Usage Alert Script

1. Programming Language: Python

2. Libraries Used:
    - time: For adding delays (sleep) in the code execution.
    - smtplib: For sending emails using the Simple Mail Transfer Protocol (SMTP).
    - psutil: For monitoring system and hardware resources like CPU, memory, disk usage, etc.
    - email.message.EmailMessage: For creating and managing email messages.
    - os : The os module provides a way of using operating system-dependent functionality like reading or writing to the file system and accessing environment variables.
    - dotenv : The dotenv package is used to read key-value pairs from a .env file and set them as environment variables. This is useful for managing configuration and sensitive data separately from the codebase.
    
3. Service Implementation:

    - Continuous Monitoring:
        The cpu() function runs an infinite loop that continuously checks the CPU usage at one-second intervals.

        The psutil.cpu_percent(1) function is used to get the CPU usage percentage over a one-second interval.

    - Sending Alerts:
        If the CPU usage exceeds 80% and an alert has not been sent (alert_sent is False), the email_alert function is called to send an email alert.
        After sending the alert, alert_sent is set to True to prevent multiple alerts for the same high CPU usage period.
        If the CPU usage drops below or equals 80%, alert_sent is reset to False, allowing for new alerts to be sent if the CPU usage exceeds 80% again in the future.

 4. Method of Sending Alerts:
    - Email:
        The email_alert function uses the smtplib library to send an email alert.
        
        It sets up the email message with the subject, body, recipient, and sender details.
        
        It connects to the Gmail SMTP server, logs in using the provided credentials, and sends the email.



## What is an SMTP Server?
SMTP stands for Simple Mail Transfer Protocol. It is a protocol used for sending email messages between servers. Most email systems that send mail over the Internet use SMTP to send messages from one server to another. The messages can then be retrieved with an email client using either POP (Post Office Protocol) or IMAP (Internet Message Access Protocol).

# How to run it? 
## Prerequisites
Python: Make sure you have Python installed on your system.
Install Required Libraries: You need to install the psutil and python-dotenv libraries if you haven't already. You can do this using pip:
```
pip install psutil python-dotenv
```

### Step 1: Create a .env File
Create a .env file in the same directory as your script. This file will store your email credentials. Add the following lines to the .env file:
do not uplode this file to git ! 

```
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_password
```

Replace your_email@gmail.com with your actual email address and your_password with your actual email password or an app-specific password if you are using Gmail with two-factor authentication.
https://support.google.com/mail/answer/185833?hl=en - to generate an app-specific password

### Step 2: Save the Script
Save your Python script in the same directory as your .env file.

### Step 3: Run the Script
Open a terminal or command prompt and navigate to the directory where your script is saved. You can then run the script using Python:
```
python cpu_monitor.py
```

### Step 4: overload the cpu to check your code (use the CPULoad.py)

