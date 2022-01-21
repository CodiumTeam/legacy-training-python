from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest, HttpRequest, HttpResponse

from src.domain.email_already_in_use_exception import EmailAlreadyInUseException
from src.domain.invalid_password_exception import InvalidPasswordException
from src.infrastructure.gmail_email_sender import GmailEmailSender
from src.use_case.register_user import RegisterUser


class UserController(View):
    # Create your views here.
    def get(self, request: HttpRequest) -> HttpResponse:
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request: HttpRequest) -> HttpResponse:
        email_sender = GmailEmailSender()
        register_user = RegisterUser(email_sender)
        try:
            user = register_user.execute(
                request.POST['password'],
                request.POST['email'],
                request.POST['name']
            )
            return JsonResponse({'name': user.name, 'email': user.email, 'id': user.id})
        except InvalidPasswordException:
            return HttpResponseBadRequest('Password is not valid')
        except EmailAlreadyInUseException:
            return HttpResponseBadRequest('The email is already in use')



