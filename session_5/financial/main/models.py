from django.db import models
from django_jalali.db import models as jmodels


class Account(models.Model):
    bank_name = models.CharField(max_length=100, verbose_name="نام بانک")
    card_number = models.CharField(max_length=16, verbose_name="شماره کارت")

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "حساب ها"


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام دسته بندی")
    icon = models.ImageField(verbose_name="ایکون")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("1", "واریزی"),
        ("2", "برداشتی"),
    )

    price = models.BigIntegerField(verbose_name="مبلغ")
    transaction_type = models.CharField(
        verbose_name="نوع", choices=TRANSACTION_TYPES, max_length=1)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="دسته بندی")
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, verbose_name="حساب")
    time = jmodels.jDateTimeField(verbose_name="تاریخ و زمان")
    objects = jmodels.jManager()

    def __str__(self):
        if self.transaction_type == "1":
            return f"مبلغ {self.price} به حساب {self.account} واریز شد ( {self.category} )"
        else:
            return f"مبلغ {self.price} از حساب {self.account} برداشت شد ( {self.category} )"

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش ها"
