# apps/goals/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Goal
from .forms import GoalForm  # Create a form for your Goal model

def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/goal_list.html', {'goals': goals})

def goal_create(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/goal_form.html', {'form': form})

def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/goal_form.html', {'form': form})

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals:goal_list')
    return render(request, 'goals/goal_confirm_delete.html', {'goal': goal})
