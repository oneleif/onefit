from django.urls import path
from .views import (
    WorkoutsListView,
    WorkoutsCreateView,
    WorkoutsDeleteView,
    WorkoutsDetailView,
    WorkoutsUpdateView,
)

urlpatterns = [
    path('', WorkoutsListView.as_view(), name='workouts-list'),
    path('new/', WorkoutsCreateView.as_view(), name='workouts-create'),
    path('<int:pk>/', WorkoutsDetailView.as_view(), name='workouts-detail'),
    path('<int:pk>/update/', WorkoutsUpdateView.as_view(), name='workouts-update'),
    path('<int:pk>/delete/', WorkoutsDeleteView.as_view(), name='workouts-delete'),
]