from django.shortcuts import render
from django.views import View
from main.models import Transaction


class MainView(View):
    def get(self, request):
        return render(request, "index.html")
