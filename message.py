# message.py

import smtplib
from email.mime.text import MIMEText

class EmailService:
    """
    Handles email setup and sending functionality.
    """
    def __init__(self, email_config):
        self.email_config = email_config

    def send_email(self, subject, message):
        """
        Sends an email with the given subject and message.
        """
        try:
            # Check if environment variables are correctly loaded
            print(f"SMTP Server: {self.email_config['smtp_server']}")
            print(f"SMTP Port: {self.email_config['smtp_port']}")
            print(f"Username: {self.email_config['username']}")
            print(f"Password: {'*' * len(self.email_config['password']) if self.email_config['password'] else 'Not Set'}")

            # Set up the email message
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.email_config['from_email']
            msg['To'] = self.email_config['to_email']
            
            # Connect to SMTP server and send email
            with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
                # Check if we can start TLS
                server.starttls()  # Optional STARTTLS encryption
                server.login(self.email_config['username'], self.email_config['password'])  # Login with env variables
                server.send_message(msg)
            
            print("Email sent successfully")
        except Exception as e:
            print(f"Error sending email: {e}")

