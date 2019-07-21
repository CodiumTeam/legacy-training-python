from app.user import User


class UserFrameworkRepository:
    repository = None

    def __init__(self) -> None:
        self.users = {}
        super().__init__()

    def save(self, user: User):
        self.users[user.email] = user

    def find_by_email(self, email_address):
        return self.users.get(email_address)

    @staticmethod
    def get_instance():
        if UserFrameworkRepository.repository is None:
            UserFrameworkRepository.repository = UserFrameworkRepository()
        return UserFrameworkRepository.repository

    @staticmethod
    def set_instance(the_instance):
        UserFrameworkRepository.repository = the_instance
