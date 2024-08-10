from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import JokeSerializer
from joke.models import Joke
import random


class JokeAPIView(APIView):
    """
        /api/
    """
    def get(self, request):
        jokes = Joke.objects.all()
        if jokes:
            target_joke = random.choice(jokes)
        else:
            target_joke = None
        serialized_data = JokeSerializer(target_joke)
        return Response(serialized_data)
