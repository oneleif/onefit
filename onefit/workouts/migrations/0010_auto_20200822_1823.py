# Generated by Django 3.0.8 on 2020-08-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0009_auto_20200822_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='user_id',
            new_name='user_name',
        ),
    ]