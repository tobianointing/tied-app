# Generated by Django 3.1.6 on 2021-02-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0002_auto_20210226_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='doctor',
        ),
    ]
