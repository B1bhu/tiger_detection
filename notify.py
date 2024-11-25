# notify.py
import smtplib
from twilio.rest import Client
from config import *

def send_sms(message):
    client = Client(twilio_account_sid, twilio_auth_token)
    for phone in phone_numbers:
        try:
            client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=phone
            )
            print(f"SMS sent successfully to {phone}")
        except Exception as e:
            print(f"Error sending SMS to {phone}: {e}")

def send_email(subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email'
    sender_password = 'your_password'

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
            print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Error sending email: {e}")

def send_notifications(message):
    send_sms(message)
    send_email("Tiger Detected", message)
