import smtplib
from email.mime.text import MIMEText
from conf import *

def msg(body, subject, recipient, username):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["To"] = recipient
    msg["From"] = username

msg(body, subject, recipient, username)

def send_email(smtp_server, smtp_port, username, password, msg):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    server.quit()

send_email(smtp_server, smtp_port, username, password, msg)