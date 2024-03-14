import unittest
from unittest.mock import Mock

from print_date import PrintDate, Calendar, Printer
from tests.printer_spy import PrinterSpy
from tests.calendar_stub import CalendarStub


class PrintDateTest(unittest.TestCase):

    def test_using_unittest_mock(self):
        calendar_stub = Mock(Calendar)
        calendar_stub.today = Mock(return_value='2024/03/14 xxxx')
        printer_spy = Mock(Printer)
        print_date = PrintDate(calendar_stub, printer_spy)

        print_date.print_current_date()

        printer_spy.print_line.assert_called_with('2024/03/14 xxxx')

    def test_without_libraries(self):
        calendar_stub = CalendarStub('2023/01/01 xxxx')
        printer_spy = PrinterSpy()
        print_date = PrintDate(calendar_stub, printer_spy)

        print_date.print_current_date()

        self.assertEqual('2023/01/01 xxxx', printer_spy.printed_text)
