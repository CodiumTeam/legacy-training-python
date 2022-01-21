from src.domain.email import Email
from src.domain.email_already_in_use_exception import EmailAlreadyInUseException
from src.domain.email_sender import EmailSender
from src.domain.invalid_password_exception import InvalidPasswordException
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from random import randint


class RegisterUser(object):

    def __init__(self, emailSender: EmailSender):
        super().__init__()
        self.email_sender = emailSender

    def execute(self, password, email, name):
        if len(password) <= 8:
            raise InvalidPasswordException()
        if "_" not in password:
            raise InvalidPasswordException()
        if UserFrameworkRepository.get_instance().find_by_email(email) is not None:
            raise EmailAlreadyInUseException()
        user = User(randint(1, 999999), name, email)
        UserFrameworkRepository.get_instance().save(user)
        email = Email('info@codium.team', email, 'Confirmation link', '')
        self.send_email(email)
        return user

    def send_email(self, email: Email):
        self.email_sender.send(email)

