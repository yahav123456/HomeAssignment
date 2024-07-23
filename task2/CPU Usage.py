import time
import smtplib
import psutil as ps
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def email_alert(subject, body, to): 
    msg = EmailMessage() 
    msg.set_content(body) 
    msg['subject'] = subject
    msg['to'] = to

    user = os.getenv('EMAIL_USER')
    msg['from'] = user
    password = os.getenv('EMAIL_PASSWORD')

    # Debug: Print the loaded environment variables
    print(f"EMAIL_USER: {user}")
    print(f"EMAIL_PASSWORD: {password}")

    # Ensure the local hostname is ASCII-compatible
    local_hostname = 'localhost'

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587, local_hostname=local_hostname)
        server.ehlo()  # Explicitly call EHLO to initiate the SMTP conversation
        server.starttls()
        server.ehlo()  # Call EHLO again after starting TLS
        server.login(user, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def cpu():
    alert_sent = False
    while True:
        cpu_use = ps.cpu_percent(1)
        if cpu_use > 1 and not alert_sent:
            email_alert("cpu alert", "HI, please note that the cpu usage is over 80% ! ", "yahavbs100@gmail.com")
            print("alert was sent")
            alert_sent = True
            time.sleep(10)
        elif cpu_use <= 80:
            alert_sent = False
            print(f'Current CPU usage: {cpu_use}%')
            time.sleep(5)

if __name__ == '__main__':
    cpu()