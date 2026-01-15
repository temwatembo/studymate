from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'priority_level', 'description', 'due_date', 'status']
        widgets = {
            'task_title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task title'
            }),
            'priority_level': forms.Select(attrs={
                'class': 'form-select'
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
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
        labels = {
            'task_title': 'Task Title',
            'priority_level': 'Priority Level',
            'description': 'Description',
            'due_date': 'Due Date',
            'status': 'Status',
        }
