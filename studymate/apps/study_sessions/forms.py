# apps/study_sessions/forms.py

from django import forms
from .models import StudySession

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['subject', 'start_time', 'end_time']
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control', 
                 'type': 'text',
                'placeholder': 'Enter session title'
            }),
            'start_time': forms.DateTimeInput(attrs={
                 'type': 'datetime-local',
                'class': 'form-control'
            }),
            'end_time': forms.DateTimeInput(attrs={
                 'type': 'datetime-local',
                'class': 'form-control'
            })
        }
        labels = {
            'subject': 'Subject',
            'start_time': 'Start Time',
            'end_time': 'End Time',
        }
