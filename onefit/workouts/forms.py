from django import forms
from django.contrib.auth.models import User
from .models import Workout
from crispy_forms.helper import FormHelper
from django.utils import timezone

class WorkoutCreateForm(forms.ModelForm):

    form_date = forms.DateTimeField(initial=timezone.now, localize=True)
    form_notes = forms.TextInput()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        super(WorkoutCreateForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit'))
        
    class Meta:
        model = Workout
        fields = ['date_created','notes']


class WorkoutsUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

