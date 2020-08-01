from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Workout(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()

    def __str__(self):
        return f'Workout : {self.date_created}'

    def get_absolute_url(self):
        return reverse('workouts-detail', kwargs={'pk': self.pk})

class Sets(models.Model):
    name = models.CharField(max_length=50)

class Set(models.Model):
    sets_id = models.ForeignKey(Sets, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    weight = models.FloatField()
    reps = models.IntegerField()

    def __str__(self):
        return f'From Set: {self.sets_id}'

class Exercise(models.Model):
    set_id = models.ForeignKey(Set, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} from set: {self.set_id}'
    

class Exercise_options(models.Model):
    name = models.CharField(max_length=50)
    body_zone = models.IntegerField()