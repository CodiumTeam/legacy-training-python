from django.http import HttpResponse
from django.views import View

class UserController(View):
    # Create your views here.
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")

    def post(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")