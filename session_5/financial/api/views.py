from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import AccountSerializer, CategorySerializer, TransactionSerializer
from main.models import Category, Account, Transaction


class AccountAPIView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serialized_data = AccountSerializer(accounts, many=True)
        return Response(serialized_data.data)


class CategoryAPIView(APIView):
    def get(self, request):
        accounts = Category.objects.all()
        serialized_data = CategorySerializer(accounts, many=True)
        return Response(serialized_data.data)


class TransactionAPIView(APIView):
    def get(self, request):
        accounts = Transaction.objects.all()
        serialized_data = TransactionSerializer(accounts, many=True)
        return Response(serialized_data.data)
