from django.shortcuts import render
from django.views import View
from main.models import Todo


class MainView(View):
    def get(self, request):
        todos = Todo.objects.all()
        return render(request, "index.html", {"todos": todos})

    def post(self, request):
        text = request.POST["text"]
        Todo.objects.create(text=text)
        return render(request, "index.html")
