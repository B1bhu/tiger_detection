import threading
from twilio.rest import Client
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

def send_sms(message, phone_numbers):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for phone in phone_numbers:
        try:
            client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=phone)
        except Exception as e:
            print(f"Failed to send SMS to {phone}: {e}")

def send_email(subject, body, email_addresses):
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    for recipient_email in email_addresses:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Failed to send email to {recipient_email}: {e}")
