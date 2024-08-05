from django.contrib import admin
from joke.models import Joke

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    pass
