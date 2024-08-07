from django.contrib import admin
from main.models import Category, Account, Transaction
from django_jalali.admin.filters import JDateFieldListFilter

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionsAdmin(admin.ModelAdmin):
    list_filter = (
        ('datetime', JDateFieldListFilter),
    )
