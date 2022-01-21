import smtplib, ssl

from src.domain.email_already_in_use_exception import EmailAlreadyInUseException
from src.domain.invalid_password_exception import InvalidPasswordException
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from random import randint


class RegisterUser(object):
    def execute(self, password, email, name):
        if len(password) <= 8:
            raise InvalidPasswordException()
        if "_" not in password:
            raise InvalidPasswordException()
        if UserFrameworkRepository.get_instance().find_by_email(email) is not None:
            raise EmailAlreadyInUseException()
        user = User(randint(1, 999999), name, email)
        UserFrameworkRepository.get_instance().save(user)
        # Send a confirmation email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail('info@codium.team', request.POST['email'], 'Confirmation link')
            pass
        return user
