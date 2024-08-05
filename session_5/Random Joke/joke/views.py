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
        return render(request, "index.html",{"joke":target_joke})
