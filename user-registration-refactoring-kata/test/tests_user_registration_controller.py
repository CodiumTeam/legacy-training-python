from django.test import RequestFactory, TestCase
from app.views import UserController
import json

class UserRegistrationControllerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_should_success_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = UserController.as_view()(request)

        self.assertEqual(response.status_code, 200)

    def test_should_returns_a_user_with_the_name_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = UserController.as_view()(request)

        content = json.loads(response.content)
        self.assertEqual(content['name'], 'Codium')

    def test_should_returns_a_user_with_the_email_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = UserController.as_view()(request)

        content = json.loads(response.content)
        self.assertEqual(content['email'], 'info@codium.team')

    def test_should_fail_when_password_is_short(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_' })

        response = UserController.as_view()(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Password is not valid')
