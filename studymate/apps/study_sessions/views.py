# apps/study_sessions/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import StudySession
from datetime import timedelta
from .forms import StudySessionForm  # Create a form for your StudySession model

def study_session_list(request):
    sessions = StudySession.objects.filter(user=request.user)
    return render(request, 'study_sessions/study_session_list.html', {'sessions': sessions})

def study_session_create(request):
    if request.method == 'POST':
        form = StudySessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user

            # Calculate session duration
            if session.start_time and session.end_time:  # Ensure both times are present
                session_duration = session.end_time - session.start_time
                session.session_duration = session_duration  # Assuming there's a 'session_duration' field in the model

            session.save()
            return redirect('study_sessions:study_session_list')
    else:
        form = StudySessionForm()
    return render(request, 'study_sessions/study_session_form.html', {'form': form})


def study_session_update(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    if request.method == 'POST':
        form = StudySessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('study_sessions:study_session_list')
    else:
        form = StudySessionForm(instance=session)
    return render(request, 'study_sessions/study_session_form.html', {'form': form})

def study_session_delete(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    if request.method == 'POST':
        session.delete()
        return redirect('study_sessions:study_session_list')
    return render(request, 'study_sessions/study_session_confirm_delete.html', {'session': session})
