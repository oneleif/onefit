# Generated by Django 3.0.8 on 2020-07-31 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200722_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise_options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body_zone', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.RenameModel(
            old_name='Exercises',
            new_name='Sets',
        ),
        migrations.RenameField(
            model_name='workout',
            old_name='date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='exercise_id',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='workout_id',
        ),
        migrations.AddField(
            model_name='exercise',
            name='name',
            field=models.CharField(default='unk', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='set_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='users.Set'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='set',
            name='sets_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Sets'),
            preserve_default=False,
        ),
    ]
