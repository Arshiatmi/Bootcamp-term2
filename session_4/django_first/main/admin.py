from django.contrib import admin
from main.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["text", "checked"]
