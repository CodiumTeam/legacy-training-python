from app.user import User


class UserFrameworkRepository:

    def __init__(self) -> None:
        super().__init__()
        self.users = {}

    def save(self, user: User):
        self.users[user.email] = user

    def find_by_email(self, email_address):
        return self.users[email_address]
