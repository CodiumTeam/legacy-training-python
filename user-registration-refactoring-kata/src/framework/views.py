import smtplib, ssl
from django.http import JsonResponse, HttpResponseBadRequest, HttpRequest, HttpResponse
from django.views import View
from src.domain.user import User
from src.infrastructure.user_framework_repository import UserFrameworkRepository
from random import randint

class UserController(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        if len(request.POST['password']) <= 8:
            return HttpResponseBadRequest('Password is not valid')
        if "_" not in request.POST['password']:
            return HttpResponseBadRequest('Password is not valid')
        if UserFrameworkRepository.get_instance().find_by_email(request.POST['email']) is not None:
            return HttpResponseBadRequest('The email is already in use')
        user = User(randint(1, 999999), request.POST['name'], request.POST['email'], request.POST['password'])
        UserFrameworkRepository.get_instance().save(user)

        # Send a confirmation email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            # Uncomment this lines with a valid username and password
            # server.login("my@gmail.com", "myPassword")
            # server.sendmail('info@codium.team', request.POST['email'], 'Confirmation link')
            pass

        return JsonResponse({'name': user.name, 'email': user.email, 'id': user.id})
