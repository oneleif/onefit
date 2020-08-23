# Generated by Django 3.0.8 on 2020-08-22 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0005_auto_20200822_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]