import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import *

def send_email(from_email, password, to_email, port, use_tls, subject, body):
    # Set up the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(EMAIL_HOST, port)
        server.ehlo()
        if use_tls:
            server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, message.as_string())
        server.close()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Email failed to send: {str(e)}")
