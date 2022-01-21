from src.domain.email import Email
from src.domain.email_sender import EmailSender
import smtplib, ssl

class GmailEmailSender(EmailSender):
    def send(self, email: Email):
        # Send a confirmation email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail(email.from_address, email.to_address, email.subject)
            pass