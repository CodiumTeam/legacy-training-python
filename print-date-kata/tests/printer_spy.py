from print_date import Printer


class PrinterSpy(Printer):

    def __init__(self):
        self.printed_text = None

    def print_line(self, line):
        self.printed_text = line
