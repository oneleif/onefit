# Generated by Django 3.0.8 on 2020-08-22 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_auto_20200822_1739'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]