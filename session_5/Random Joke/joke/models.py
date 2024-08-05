from django.db import models

class Joke(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "جک"
        verbose_name_plural = "جک ها"
