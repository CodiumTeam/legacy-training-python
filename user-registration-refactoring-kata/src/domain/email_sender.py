import abc

from src.domain.email import Email


class EmailSender(abc.ABC):
    @abc.abstractmethod
    def send(self, email: Email):
        pass
