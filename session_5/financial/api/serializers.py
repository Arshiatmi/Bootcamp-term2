from rest_framework import serializers
from main.models import Account,Category,Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    account = AccountSerializer()

    class Meta:
        model = Transaction
        fields = "__all__"
