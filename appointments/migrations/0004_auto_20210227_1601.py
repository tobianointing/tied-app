# Generated by Django 3.1.6 on 2021-02-27 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20210226_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 27, 16, 1, 31, 140271)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 27, 16, 1, 31, 140271)),
        ),
    ]
