from rest_framework import routers
from .api import (
    ExerciseViewset, SetViewset, WorkoutViewset,
)

router = routers.DefaultRouter()
router.register('api/workouts', WorkoutViewset, 'workouts')
router.register('api/sets', SetViewset, 'sets')
router.register('api/exercises', ExerciseViewset, 'exercises')
router.register('api/exercise_options', WorkoutViewset, 'workouts')

urlpatterns = router.urls