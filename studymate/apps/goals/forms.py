# apps/goals/forms.py

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_title', 'description', 'due_date', 'progress_percentage']  # Adjust fields as necessary

        widgets = {
            'goal_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter goal title'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Enter a brief description'
            }),
            'due_date': forms.TextInput(attrs={
                'type': 'date',  # HTML5 date input
                'class': 'form-control'
            }),
            'progress_percentage': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'goal_title': 'Goal Title',
            'description': 'Description',
            'due_date': 'Due Date',
            'progress_percentage': 'Progress %',
        }
