# Generated by Django 2.1 on 2018-08-21 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20180820_0034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='foto',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='game',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 21, 23, 48, 44, 970457, tzinfo=utc)),
        ),
    ]
