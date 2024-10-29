# apps/reminders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Reminder
from .forms import ReminderForm  # Create a form for your Reminder model

def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminders/reminder_list.html', {'reminders': reminders})

def reminder_create(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminders:reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/reminder_form.html', {'form': form})

def reminder_update(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminders:reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/reminder_form.html', {'form': form})

def reminder_delete(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders:reminder_list')
    return render(request, 'reminders/reminder_confirm_delete.html', {'reminder': reminder})
