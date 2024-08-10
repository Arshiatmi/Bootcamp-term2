from django.urls import path
from main.views import MainView,TodoCheckView,TodoDeleteView,TodoChangeView

urlpatterns = [
    path('', MainView.as_view()),
    path('todo/check/', TodoCheckView.as_view()),
    path('todo/delete/', TodoDeleteView.as_view()),
    path('todo/change/', TodoChangeView.as_view()),
]
