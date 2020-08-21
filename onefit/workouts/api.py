from rest_framework import viewsets, permissions
from workouts.models import (
    Workout,
    Set,
    Exercise,
    Exercise_options,
)
from .serializers import (
    ExerciseSerializer, 
    Exercise_optionsSerializer, 
    SetSerializer, 
    WorkoutSerializer,
)

class WorkoutViewset(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WorkoutSerializer

class SetViewset(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SetSerializer

class ExerciseViewset(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ExerciseSerializer

class Exercise_optionsViewset(viewsets.ModelViewSet):
    queryset = Exercise_options.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Exercise_optionsSerializer


