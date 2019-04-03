import smtplib, ssl
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from app.user import User
from app.user_framework_repository import UserFrameworkRepository
from random import randint

class UserController(View):
    user_repository = UserFrameworkRepository()

    # Create your views here.
    def get(self, request):
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request):
        if len(request.POST['password']) <= 8:
            return HttpResponseBadRequest('Password is not valid')
        if "_" not in request.POST['password']:
            return HttpResponseBadRequest('Password is not valid')
        if self.user_repository.find_by_email(request.POST['email']) is not None:
            return HttpResponseBadRequest('The email is already in use')
        user = User(randint(1, 999999), request.POST['name'], request.POST['email'])
        self.user_repository.save(user)

        # Send a confirmation email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail('info@codium.team', request.POST['email'], 'Confirmation link')
            pass

        return JsonResponse({'name': user.name, 'email': user.email, 'id': user.id})
