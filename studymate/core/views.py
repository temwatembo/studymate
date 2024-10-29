from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password  # Import make_password for hashing passwords
from .models import User
from apps.goals.models import Goal
from apps.study_sessions.models import StudySession
from apps.tasks.models import Task
from apps.reminders.models import Reminder
from .forms import UserRegistrationForm  # Import the registration form

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'core_pages/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'core_pages/register.html', {'form': form})  # Pass the form to the template

@login_required
def dashboard(request):
    user = request.user
    goals = Goal.objects.filter(user=user)
    sessions = StudySession.objects.filter(user=user)
    tasks = Task.objects.filter(user=user)
    reminders = Reminder.objects.filter(user=user)
    
    context = {
        'goals': goals,
        'sessions': sessions,
        'tasks': tasks,
        'reminders': reminders,
    }
    return render(request, 'core_pages/dashboard.html', context)

def frontpage(request):
    return render(request, 'basic/front_page.html')
