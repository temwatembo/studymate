# apps/goals/forms.py

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_title', 'description', 'due_date', 'progress_percentage']  # Adjust fields as necessary
