# Generated by Django 2.1 on 2018-08-20 00:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 20, 0, 17, 11, 806927, tzinfo=utc)),
        ),
    ]
