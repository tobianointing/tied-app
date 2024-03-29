# Generated by Django 3.1.6 on 2021-02-26 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('queries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='email',
        ),
        migrations.AlterField(
            model_name='query',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_query', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='query',
            name='teider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teider_query', to=settings.AUTH_USER_MODEL),
        ),
    ]
