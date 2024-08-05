from django.contrib import admin
from main.models import Category, Account, Transactions

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass
