# Generated by Django 3.0.8 on 2020-08-22 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200731_1932'),
        ('workouts', '0007_delete_ofuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
