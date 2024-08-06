from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views import View
from main.models import Todo


class MainView(View):
    def get(self, request):
        todos = Todo.objects.all()
        checked_count = len(Todo.objects.filter(checked=True))
        return render(request, "index.html", {"todos": todos, "checked_count": checked_count})

    def post(self, request):
        text = request.POST["text"]
        Todo.objects.create(text=text)
        return redirect("/")


class TodoCheckView(View):
    def get(self, request):
        pk = request.GET["pk"]
        obj = get_object_or_404(Todo, pk=pk)
        if obj.checked:
            obj.checked = False
        else:
            obj.checked = True
        return redirect("/")


class TodoDeleteView(View):
    def get(self, request):
        pk = request.GET["pk"]
        obj = get_object_or_404(Todo, pk=pk)
        obj.delete()
        return redirect("/")


class TodoChangeView(View):
    def get(self, request):
        pk = request.GET["pk"]
        text = request.GET["text"]
        obj = get_object_or_404(Todo, pk=pk)
        obj.text = text
        obj.save()
        return redirect("/")
