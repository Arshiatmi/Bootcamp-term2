# Generated by Django 5.0.7 on 2024-07-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'لیست کار', 'verbose_name_plural': 'لیست کار ها'},
        ),
        migrations.AlterField(
            model_name='todo',
            name='checked',
            field=models.BooleanField(default=False, verbose_name='انجام شدن'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(verbose_name='متن'),
        ),
    ]