class Email(object):

    def __init__(self, from_address, to_address, subject, body):
        self.body = body
        self.subject = subject
        self.to_address = to_address
        self.from_address = from_address