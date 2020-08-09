from rest_framework import serializers
from workouts.models import (
    Workout,
    Set,
    Exercise,
    Exercise_options
)

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class Exercise_optionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise_options
        fields = '__all__'