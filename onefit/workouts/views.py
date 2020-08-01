from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Workout
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


class WorkoutsListView(LoginRequiredMixin, ListView):
    model = Workout
    template_name = 'workouts/workouts.html'
    context_object_name = 'workouts'
    ordering = ['-date_created']

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user)

class WorkoutsDetailView(LoginRequiredMixin, DetailView):
    model = Workout

class WorkoutsCreateView(LoginRequiredMixin, CreateView):
    model = Workout
    fields = ['date_created', 'notes']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

class WorkoutsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Workout
    fields = ['user_id', 'notes']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Workout = self.get_object()
        if self.request.user == Workout.user_id:
            return True
        return False

class WorkoutsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Workout
    success_url = '/workouts/'

    def test_func(self):
        Workout = self.get_object()
        if self.request.user == Workout.user_id:
            return True
        return False
