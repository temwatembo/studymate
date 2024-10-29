# apps/reminders/forms.py

from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['reminder_message', 'reminder_time']  # Adjust fields as necessary
