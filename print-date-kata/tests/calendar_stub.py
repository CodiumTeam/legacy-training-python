from print_date import Calendar


class CalendarStub(Calendar):

    def __init__(self, returned_date):
        super().__init__()
        self.returned_date = returned_date

    def today(self):
        return self.returned_date
