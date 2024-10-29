# apps/tasks/forms.py

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'priority_level', 'description', 'due_date', 'status']  
