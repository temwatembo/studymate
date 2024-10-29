# apps/study_sessions/forms.py

from django import forms
from .models import StudySession

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['subject', 'start_time', 'end_time', 'session_duration']  # Adjust fields as necessary
