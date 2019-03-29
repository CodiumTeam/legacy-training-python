from django.test import RequestFactory, TestCase
from app.views import UserController

class UserRegistrationControllerTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_xxx(self):
        request = self.factory.post('/users', {'name': 'Codium', 'email': 'info@codium.team', 'password': 'myPass_123123' })
        response = UserController.as_view()(request)
        self.assertEqual(response.status_code, 200)
