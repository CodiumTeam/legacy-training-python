from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from app.user import User

class UserController(View):
    # Create your views here.
    def get(self, request):
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request):
        if len(request.POST['password']) <= 8:
            return HttpResponseBadRequest('Password is not valid')
        if "_" not in request.POST['password']:
            return HttpResponseBadRequest('Password is not valid')
        user = User(request.POST['name'], request.POST['email'])
        return JsonResponse({'name': user.name, 'email': user.email})