# Generated by Django 3.1.6 on 2021-03-18 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0012_auto_20210318_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 18, 17, 57, 7, 623041)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 18, 17, 57, 7, 623041)),
        ),
    ]
