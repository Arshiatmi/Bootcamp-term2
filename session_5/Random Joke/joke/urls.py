from django.urls import path
from joke.views import LoginView, MainView, RegisterView

urlpatterns = [
    path('', MainView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
]
