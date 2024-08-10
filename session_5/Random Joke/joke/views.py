from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from joke.models import Joke
import random


class MainView(View):
    def get(self, request):
        jokes = Joke.objects.all()
        if jokes:
            target_joke = random.choice(jokes)
        else:
            target_joke = None
        return render(request, "index.html", {"joke": target_joke})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(username, email, password)
        return render(request, "index.html")
