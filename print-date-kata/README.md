# Goal
Unit test the printCurrentDate function.

1. Test the code with doubles from a library.
2. Test the code with doubles created by you.
# Code to test
    class PrintDate:
        def __init__(self, calendar, printer):
            self.printer = printer
            self.calendar = calendar
    
        def print_current_date(self):
            self.printer.print_line(self.calendar.today())

# Learnings
How to build a Mock and Stub manually.

How to use Unittest Mock to generate the doubles.

## Tools
[Unittest documentation](https://cpython-test-docs.readthedocs.io/en/latest/library/unittest.mock.html)
### Example of spy

    def test_should_send_an_email(self):
        emailSender = Mock(EmailSender)
        user_registration = UserRegistration(email_sender)
    
        user_registration.register()
    
        email_sender.send.assert_called()

	
### Example of stub

    def test_should_success_when_password_is_valid(self):
        password_validator = Mock(PasswordValidator)
        password_validator.is_valid = Mock(return_value=true)
        user_registration = UserRegistration(password_validator)

        success = user_registration.register()

        assertTrue(success)

## How to run and see the result

    make 
    
or open [Makefile](./Makefile) and execute the one you want.

## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)
