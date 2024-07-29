from django.db import models

class Todo(models.Model):
    text = models.TextField(verbose_name="متن")
    checked = models.BooleanField(verbose_name="انجام شدن",default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "لیست کار"
        verbose_name_plural = "لیست کار ها"
