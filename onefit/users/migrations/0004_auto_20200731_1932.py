# Generated by Django 3.0.8 on 2020-07-31 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200731_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='set_id',
        ),
        migrations.DeleteModel(
            name='Exercise_options',
        ),
        migrations.RemoveField(
            model_name='set',
            name='sets_id',
        ),
        migrations.RemoveField(
            model_name='workout',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='Set',
        ),
        migrations.DeleteModel(
            name='Sets',
        ),
        migrations.DeleteModel(
            name='Workout',
        ),
    ]