from django.db import models


class Account(models.Model):
    bank_name = models.CharField(max_length=100, verbose_name="نام بانک")
    card_number = models.CharField(max_length=16, verbose_name="شماره کارت")


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته بندی")
    icon = models.ImageField(verbose_name="ایکون")


class Transactions(models.Model):
    price = models.BigIntegerField(verbose_name="مبلغ")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name="حساب")
    time = models.DateTimeField(verbose_name="تاریخ و زمان")
