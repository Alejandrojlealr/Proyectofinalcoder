# Generated by Django 3.2.9 on 2021-12-08 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPfinalcoder', '0002_auto_20211128_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakery',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 10, 54, 12, 254967)),
        ),
        migrations.AddField(
            model_name='cakes',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 10, 54, 12, 251971)),
        ),
        migrations.AddField(
            model_name='dessert',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 10, 54, 12, 252969)),
        ),
    ]
