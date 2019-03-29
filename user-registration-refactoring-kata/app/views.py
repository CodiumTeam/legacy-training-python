from django.http import JsonResponse
from django.views import View
from app.user import User

class UserController(View):
    # Create your views here.
    def get(self, request):
        return JsonResponse("Hello, world. You're at the polls index.")

    def post(self, request):
        user = User(request.POST['name'])
        return JsonResponse({'name': user.name})