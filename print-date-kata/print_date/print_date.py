class PrintDate:

    def __init__(self, calendar, printer):
        self.printer = printer
        self.calendar = calendar

    def print_current_date(self):
        self.printer.print_line(self.calendar.today())