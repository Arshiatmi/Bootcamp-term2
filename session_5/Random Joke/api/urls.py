from django.urls import path
from api.views import JokeAPIView

urlpatterns = [
    path('api/', JokeAPIView.as_view()),
]
