import unittest
from print_date import PrintDate, Calendar, Printer

class PrintDateTest(unittest.TestCase):

    def test_xxx(self):
        print_date = PrintDate(Calendar(), Printer())

        print_date.print_current_date()

        # I don't know how to test it