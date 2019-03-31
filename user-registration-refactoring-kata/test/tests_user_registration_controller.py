from django.test import RequestFactory, TestCase

from app.user import User
from app.user_framework_repository import UserFrameworkRepository
from app.views import UserController
import json

class UserRegistrationControllerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        UserController.user_repository = UserFrameworkRepository()
        self.view = UserController.as_view()

    def test_should_success_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = self.view(request)

        self.assertEqual(response.status_code, 200)

    def test_should_returns_a_user_with_the_name_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = self.view(request)

        content = json.loads(response.content)
        self.assertEqual(content['name'], 'Codium')

    def test_should_returns_a_user_with_the_email_when_everything_is_valid(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })

        response = self.view(request)

        content = json.loads(response.content)
        self.assertEqual(content['email'], 'info@codium.team')

    def test_should_fail_when_password_is_short(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_' })

        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Password is not valid')

    def test_should_fail_when_password_does_not_contain_underscore(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass123123' })

        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'Password is not valid')

    def test_persist_the_user(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })
        self.view(request)

        user = UserController.user_repository.find_by_email('info@codium.team')
        self.assertIsNotNone(user)

    def test_should_fail_when_email_is_used(self):
        UserController.user_repository.save(User('Codium', 'info@codium.team'))

        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })
        response = self.view(request)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'The email is already in use')
