from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    UNITS_OPT = (
        ('LBS','Pounds'),
        ('KG','Kilograms'),
    )
    units = models.CharField(max_length=3, choices=UNITS_OPT)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        #Image resizing
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Workout(models.Model):
    date = models.DateTimeField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField()

class Exercises(models.Model):
    name = models.CharField(max_length=50)

class Exercise(models.Model):
    workout_id = models.ForeignKey(Workout, on_delete=models.CASCADE)
    order = models.IntegerField(unique=True)
    exercise_id = models.ForeignKey(Exercises, on_delete=models.CASCADE)

class Set(models.Model):
    order = models.IntegerField(unique=True)
    weight = models.FloatField()
    reps = models.IntegerField()
