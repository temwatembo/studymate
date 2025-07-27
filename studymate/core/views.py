from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.hashers import make_password  # Import make_password for hashing passwords
from .models import User
from apps.goals.models import Goal
from apps.study_sessions.models import StudySession
from apps.tasks.models import Task
from apps.reminders.models import Reminder
from .forms import UserRegistrationForm  # Import the registration form
from django.db.models import Q, Avg, Count, Sum
from django.utils import timezone
from datetime import datetime, timedelta
from collections import defaultdict
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
import json


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)

            # Redirect based on user role
            if user.is_staff or user.is_superuser:
                return redirect('admin_dashboard')  # Replace with your actual admin page
            else:
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

from datetime import timedelta

@login_required
def dashboard(request):
    user = request.user
    goals = Goal.objects.filter(user=user)
    sessions = StudySession.objects.filter(user=user)
    tasks = Task.objects.filter(user=user)
    reminders = Reminder.objects.filter(user=user)

    # Calculate total study hours
    total_study_time = timedelta()  # Initialize as a timedelta object
    for session in sessions:
        if session.start_time and session.end_time:  # Ensure both times exist
            total_study_time += session.end_time - session.start_time

    # Convert total study time to hours and minutes
    total_hours = total_study_time.total_seconds() // 3600
    total_minutes = (total_study_time.total_seconds() % 3600) // 60

    context = {
        'goals': goals,
        'sessions': sessions,
        'tasks': tasks,
        'reminders': reminders,
        'total_study_hours': total_hours,
        'total_study_minutes': total_minutes,
    }
    return render(request, 'core_pages/dashboard.html', context)

def frontpage(request):
    return render(request, 'basic/front_page.html')



@login_required
def progress_report(request):
    user = request.user
    current_date = timezone.now().date()
    
    # Basic metrics
    goals = Goal.objects.filter(user=user)
    tasks = Task.objects.filter(user=user)
    study_sessions = StudySession.objects.filter(user=user)
    
    total_goals = goals.count()
    completed_goals = goals.filter(status='completed').count()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    
    # Calculate total study hours
    total_study_duration = study_sessions.aggregate(
        total=Sum('session_duration')
    )['total'] or timedelta(0)
    total_study_hours = round(total_study_duration.total_seconds() / 3600, 1)
    
    # Completion rates
    goal_completion_rate = round((completed_goals / total_goals * 100) if total_goals > 0 else 0, 1)
    task_completion_rate = round((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0, 1)
    
    # Average goal progress
    average_goal_progress = goals.aggregate(
        avg_progress=Avg('progress_percentage')
    )['avg_progress'] or 0
    average_goal_progress = round(float(average_goal_progress), 1)
    
    # Performance level
    overall_score = (goal_completion_rate + task_completion_rate + average_goal_progress) / 3
    if overall_score >= 80:
        performance_level = "Excellent"
        performance_class = "badge-excellent"
    elif overall_score >= 60:
        performance_level = "Good"
        performance_class = "badge-good"
    else:
        performance_level = "Needs Improvement"
        performance_class = "badge-needs-improvement"
    
    # Study session analytics
    study_sessions_count = study_sessions.count()
    
    # Average session duration
    if study_sessions_count > 0:
        avg_duration = total_study_duration / study_sessions_count
        average_session_duration = round(avg_duration.total_seconds() / 3600, 1)
    else:
        average_session_duration = 0
    
    # Most studied subject
    subject_counts = study_sessions.values('subject').annotate(
        total_duration=Sum('session_duration'),
        session_count=Count('id')
    ).order_by('-total_duration')
    
    most_studied_subject = subject_counts.first()['subject'] if subject_counts else 'None'
    
    # Subject statistics
    subject_stats = []
    if subject_counts:
        total_subject_time = sum(s['total_duration'].total_seconds() for s in subject_counts)
        for subject in subject_counts[:5]:  # Top 5 subjects
            hours = round(subject['total_duration'].total_seconds() / 3600, 1)
            percentage = round((subject['total_duration'].total_seconds() / total_subject_time) * 100, 1)
            subject_stats.append({
                'subject': subject['subject'],
                'hours': hours,
                'percentage': percentage
            })
    
    # Recent activities
    recent_activities = []
    
    # Recent completed goals
    recent_goals = goals.filter(
        status='completed',
        updated_at__gte=timezone.now() - timedelta(days=7)
    ).order_by('-updated_at')[:3]
    
    for goal in recent_goals:
        recent_activities.append({
            'title': f'Completed Goal: {goal.goal_title}',
            'description': goal.description[:50] + '...' if len(goal.description) > 50 else goal.description,
            'date': goal.updated_at,
            'type': 'success',
            'category': 'Goal'
        })
    
    # Recent completed tasks
    recent_tasks = tasks.filter(
        status='Completed',
        updated_at__gte=timezone.now() - timedelta(days=7)
    ).order_by('-updated_at')[:3]
    
    for task in recent_tasks:
        recent_activities.append({
            'title': f'Completed Task: {task.task_title}',
            'description': task.description,
            'date': task.updated_at,
            'type': 'primary',
            'category': 'Task'
        })
    
    # Recent study sessions
    recent_sessions = study_sessions.filter(
        created_at__gte=timezone.now() - timedelta(days=7)
    ).order_by('-created_at')[:3]
    
    for session in recent_sessions:
        duration_hours = round(session.session_duration.total_seconds() / 3600, 1)
        recent_activities.append({
            'title': f'Study Session: {session.subject}',
            'description': f'Studied for {duration_hours} hours',
            'date': session.created_at,
            'type': 'info',
            'category': 'Study'
        })
    
    # Sort recent activities by date
    recent_activities.sort(key=lambda x: x['date'], reverse=True)
    recent_activities = recent_activities[:10]  # Limit to 10 most recent
    
    # Generate insights
    insights = generate_insights(user, goals, tasks, study_sessions, overall_score)
    
    # Generate recommendations
    recommendations = generate_recommendations(
        user, goals, tasks, study_sessions, goal_completion_rate, 
        task_completion_rate, average_goal_progress
    )
    
    # Upcoming deadlines
    upcoming_deadlines = get_upcoming_deadlines(goals, tasks)
    
    # Weekly goal tracking
    week_start = current_date - timedelta(days=current_date.weekday())
    week_end = week_start + timedelta(days=6)
    
    current_week_sessions = study_sessions.filter(
        start_time__date__range=[week_start, week_end]
    )
    current_week_duration = current_week_sessions.aggregate(
        total=Sum('session_duration')
    )['total'] or timedelta(0)
    current_week_hours = round(current_week_duration.total_seconds() / 3600, 1)
    
    weekly_goal_hours = 20  # Default weekly goal, can be made configurable
    weekly_progress = min(round((current_week_hours / weekly_goal_hours) * 100, 1), 100)
    
    context = {
        'current_date': current_date,
        'total_goals': total_goals,
        'completed_goals': completed_goals,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'total_study_hours': total_study_hours,
        'goal_completion_rate': goal_completion_rate,
        'task_completion_rate': task_completion_rate,
        'average_goal_progress': average_goal_progress,
        'performance_level': performance_level,
        'performance_class': performance_class,
        'study_sessions_count': study_sessions_count,
        'average_session_duration': average_session_duration,
        'most_studied_subject': most_studied_subject,
        'subject_stats': subject_stats,
        'recent_activities': recent_activities,
        'insights': insights,
        'recommendations': recommendations,
        'upcoming_deadlines': upcoming_deadlines,
        'weekly_goal_hours': weekly_goal_hours,
        'current_week_hours': current_week_hours,
        'weekly_progress': weekly_progress,
    }
    
    return render(request, 'basic/progress_report.html', context)


def generate_insights(user, goals, tasks, study_sessions, overall_score):
    """Generate personalized insights based on user data"""
    insights = []
    
    # Goal-related insights
    in_progress_goals = goals.filter(status='in_progress').count()
    overdue_goals = goals.filter(due_date__lt=timezone.now().date(), status__in=['pending', 'in_progress']).count()
    
    if overdue_goals > 0:
        insights.append(f"You have {overdue_goals} overdue goal{'s' if overdue_goals > 1 else ''}. Consider reviewing and updating them.")
    
    if in_progress_goals > 5:
        insights.append("You have many goals in progress. Focus on completing a few before starting new ones.")
    
    # Task-related insights
    high_priority_pending = tasks.filter(priority_level='High', status='Pending').count()
    if high_priority_pending > 0:
        insights.append(f"You have {high_priority_pending} high-priority task{'s' if high_priority_pending > 1 else ''} pending attention.")
    
    # Study session insights
    if study_sessions.exists():
        # Check study consistency
        last_week = timezone.now() - timedelta(days=7)
        recent_sessions = study_sessions.filter(created_at__gte=last_week).count()
        
        if recent_sessions == 0:
            insights.append("You haven't had any study sessions this week. Try to maintain regular study habits.")
        elif recent_sessions >= 5:
            insights.append("Great job maintaining consistent study sessions this week!")
        
        # Subject diversity
        unique_subjects = study_sessions.values('subject').distinct().count()
        if unique_subjects == 1:
            insights.append("Consider diversifying your study subjects for a more balanced learning approach.")
    
    # Performance insights
    if overall_score >= 80:
        insights.append("Excellent performance! You're maintaining high completion rates across all areas.")
    elif overall_score < 50:
        insights.append("Your completion rates could use improvement. Consider breaking tasks into smaller, manageable pieces.")
    
    return insights[:5]  # Limit to 5 insights


def generate_recommendations(user, goals, tasks, study_sessions, goal_rate, task_rate, avg_progress):
    """Generate personalized recommendations"""
    recommendations = []
    
    # Goal recommendations
    if goal_rate < 50:
        recommendations.append("Try breaking down large goals into smaller, more achievable milestones.")
    
    if avg_progress < 50:
        recommendations.append("Update your goal progress regularly to stay motivated and track advancement.")
    
    # Task recommendations
    if task_rate < 60:
        recommendations.append("Prioritize high-impact tasks and use time-blocking to improve completion rates.")
    
    pending_tasks = tasks.filter(status='Pending').count()
    if pending_tasks > 10:
        recommendations.append("Consider reducing your task backlog by completing or removing outdated tasks.")
    
    # Study recommendations
    if study_sessions.exists():
        avg_session_duration = study_sessions.aggregate(
            avg_duration=Avg('session_duration')
        )['avg_duration']
        
        if avg_session_duration:
            avg_hours = avg_session_duration.total_seconds() / 3600
            if avg_hours < 1:
                recommendations.append("Try extending your study sessions to at least 1 hour for better focus and retention.")
            elif avg_hours > 4:
                recommendations.append("Consider shorter, more frequent study sessions to prevent burnout and maintain focus.")
    else:
        recommendations.append("Start tracking your study sessions to get better insights into your learning patterns.")
    
    # Weekly activity recommendation
    last_week_sessions = study_sessions.filter(
        created_at__gte=timezone.now() - timedelta(days=7)
    ).count()
    
    if last_week_sessions < 3:
        recommendations.append("Aim for at least 3-4 study sessions per week to maintain consistent learning momentum.")
    
    return recommendations[:5]  # Limit to 5 recommendations


def get_upcoming_deadlines(goals, tasks):
    """Get upcoming deadlines for goals and tasks"""
    upcoming = []
    current_date = timezone.now().date()
    
    # Upcoming goal deadlines
    upcoming_goals = goals.filter(
        due_date__gte=current_date,
        status__in=['pending', 'in_progress']
    ).order_by('due_date')[:5]
    
    for goal in upcoming_goals:
        days_left = (goal.due_date - current_date).days
        urgency = 'danger' if days_left <= 3 else 'warning' if days_left <= 7 else 'info'
        upcoming.append({
            'title': goal.goal_title,
            'type': 'Goal',
            'days_left': days_left,
            'urgency': urgency,
            'due_date': goal.due_date
        })
    
    # Upcoming task deadlines
    upcoming_tasks = tasks.filter(
        due_date__gte=current_date,
        status='Pending'
    ).order_by('due_date')[:5]
    
    for task in upcoming_tasks:
        days_left = (task.due_date - current_date).days
        urgency = 'danger' if days_left <= 3 else 'warning' if days_left <= 7 else 'info'
        upcoming.append({
            'title': task.task_title,
            'type': 'Task',
            'days_left': days_left,
            'urgency': urgency,
            'due_date': task.due_date
        })
    
    # Sort by due date and return top 8
    upcoming.sort(key=lambda x: x['due_date'])
    return upcoming[:8]

# Helper function to check if the user is staff or superuser
def is_admin_user(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_admin_user, login_url='dashboard')  # redirect unauthorized users
def admin_dashboard(request):
    # Get current date and time
    now = timezone.now()
    today = now.date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    # Total users count
    total_users = User.objects.count()
    
    # Active users (users who logged in within the last 7 days)
    # Note: This requires you to track last_login or create a UserActivity model
    active_users = User.objects.filter(last_login__gte=week_ago).count() if hasattr(User, 'last_login') else 0
    
    # New users this month
    new_users_this_month = User.objects.filter(created_at__gte=month_ago).count()
    
    # Staff members count
    staff_count = User.objects.filter(is_staff=True).count()
    
    # Superusers count
    superuser_count = User.objects.filter(is_superuser=True).count()
    
    # User registration trend (last 7 days)
    registration_trend = []
    for i in range(7):
        date = today - timedelta(days=i)
        count = User.objects.filter(created_at__date=date).count()
        registration_trend.append({
            'date': date.strftime('%m/%d'),
            'count': count
        })
    registration_trend.reverse()  # Most recent first
    
    # User role distribution
    regular_users = total_users - staff_count
    
    context = {
        'total_users': total_users,
        'active_users': active_users,
        'new_users_this_month': new_users_this_month,
        'staff_count': staff_count,
        'superuser_count': superuser_count,
        'regular_users': regular_users,
        'registration_trend': registration_trend,
        'current_time': now,
    }
    
    return render(request, 'core_pages/admin/admin_dashboard.html', context)


@login_required
def users_list(request):
    users = User.objects.all().order_by('-created_at')  # Or filter as needed
    print(users.query)
    return render(request, 'core_pages/admin/users_list.html', {'users': users})




@login_required
@user_passes_test(is_admin_user, login_url='dashboard')  # redirect unauthorized users
def analytics_dashboard(request):
    # Get current date and time ranges
    now = timezone.now()
    today = now.date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    three_months_ago = today - timedelta(days=90)
    year_ago = today - timedelta(days=365)
    
    # User Registration Analytics
    total_users = User.objects.count()
    users_this_week = User.objects.filter(created_at__gte=week_ago).count()
    users_this_month = User.objects.filter(created_at__gte=month_ago).count()
    users_this_quarter = User.objects.filter(created_at__gte=three_months_ago).count()
    
    # Calculate growth rates
    users_last_week = User.objects.filter(
        created_at__gte=week_ago - timedelta(days=7),
        created_at__lt=week_ago
    ).count()
    users_last_month = User.objects.filter(
        created_at__gte=month_ago - timedelta(days=30),
        created_at__lt=month_ago
    ).count()
    
    weekly_growth = ((users_this_week - users_last_week) / max(users_last_week, 1)) * 100
    monthly_growth = ((users_this_month - users_last_month) / max(users_last_month, 1)) * 100
    
    # User Activity Analytics
    active_users_week = User.objects.filter(last_login__gte=week_ago).count() if hasattr(User, 'last_login') else 0
    active_users_month = User.objects.filter(last_login__gte=month_ago).count() if hasattr(User, 'last_login') else 0
    
    # User Role Distribution
    superusers = User.objects.filter(is_superuser=True).count()
    staff_users = User.objects.filter(is_staff=True, is_superuser=False).count()
    regular_users = total_users - superusers - staff_users
    
    # Monthly Registration Data (Last 12 months)
    monthly_registrations = []
    for i in range(12):
        start_date = (today.replace(day=1) - timedelta(days=30*i)).replace(day=1)
        if i == 0:
            end_date = today
        else:
            next_month = start_date.replace(month=start_date.month % 12 + 1) if start_date.month < 12 else start_date.replace(year=start_date.year + 1, month=1)
            end_date = next_month - timedelta(days=1)
        
        count = User.objects.filter(
            created_at__date__gte=start_date,
            created_at__date__lte=end_date
        ).count()
        
        monthly_registrations.append({
            'month': start_date.strftime('%b %Y'),
            'count': count,
            'date': start_date.isoformat()
        })
    
    monthly_registrations.reverse()  # Most recent first
    
    # Weekly Registration Data (Last 8 weeks)
    weekly_registrations = []
    for i in range(8):
        start_date = today - timedelta(days=7*(i+1))
        end_date = today - timedelta(days=7*i)
        
        count = User.objects.filter(
            created_at__date__gte=start_date,
            created_at__date__lt=end_date
        ).count()
        
        weekly_registrations.append({
            'week': f"Week {i+1}",
            'period': f"{start_date.strftime('%m/%d')} - {end_date.strftime('%m/%d')}",
            'count': count
        })
    
    weekly_registrations.reverse()
    
    # Daily Registration Data (Last 30 days)
    daily_registrations = []
    for i in range(30):
        date = today - timedelta(days=i)
        count = User.objects.filter(created_at__date=date).count()
        daily_registrations.append({
            'date': date.strftime('%m/%d'),
            'full_date': date.isoformat(),
            'count': count,
            'day_name': date.strftime('%a')
        })
    
    daily_registrations.reverse()
    
    # Top Registration Days (Day of week analysis)
    day_of_week_stats = []
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i, day in enumerate(days):
        count = User.objects.filter(created_at__week_day=i+2).count()  # Django week_day starts from Sunday=1
        day_of_week_stats.append({
            'day': day,
            'count': count,
            'percentage': (count / max(total_users, 1)) * 100
        })
    
    # User Engagement Metrics
    engagement_metrics = {
        'total_users': total_users,
        'active_this_week': active_users_week,
        'active_this_month': active_users_month,
        'engagement_rate_week': (active_users_week / max(total_users, 1)) * 100,
        'engagement_rate_month': (active_users_month / max(total_users, 1)) * 100,
    }
    
    # Recent Activity Summary
    recent_activity = []
    
    # Get recent registrations
    recent_users = User.objects.order_by('-created_at')[:5]
    for user in recent_users:
        recent_activity.append({
            'type': 'registration',
            'message': f"New user {user.first_name or user.last_name} registered",
            'time': user.created_at,
            'icon': 'person-plus',
            'color': 'success'
        })
    
    # Sort by time
    recent_activity.sort(key=lambda x: x['time'], reverse=True)
    recent_activity = recent_activity[:10]  # Limit to 10 items
    
    # Prepare data for charts (convert to JSON for JavaScript)
    chart_data = {
        'monthly_registrations': json.dumps(monthly_registrations),
        'weekly_registrations': json.dumps(weekly_registrations),
        'daily_registrations': json.dumps(daily_registrations),
        'day_of_week_stats': json.dumps(day_of_week_stats),
        'role_distribution': json.dumps([
            {'label': 'Regular Users', 'value': regular_users, 'color': '#667eea'},
            {'label': 'Staff', 'value': staff_users, 'color': '#764ba2'},
            {'label': 'Superusers', 'value': superusers, 'color': '#f093fb'}
        ])
    }
    
    context = {
        # Basic metrics
        'total_users': total_users,
        'users_this_week': users_this_week,
        'users_this_month': users_this_month,
        'users_this_quarter': users_this_quarter,
        'weekly_growth': round(weekly_growth, 1),
        'monthly_growth': round(monthly_growth, 1),
        
        # Activity metrics
        'active_users_week': active_users_week,
        'active_users_month': active_users_month,
        'engagement_metrics': engagement_metrics,
        
        # Role distribution
        'superusers': superusers,
        'staff_users': staff_users,
        'regular_users': regular_users,
        
        # Chart data
        'chart_data': chart_data,
        'monthly_registrations': monthly_registrations,
        'weekly_registrations': weekly_registrations,
        'daily_registrations': daily_registrations,
        'day_of_week_stats': day_of_week_stats,
        
        # Activity
        'recent_activity': recent_activity,
        
        # Metadata
        'current_time': now,
        'report_period': f"{month_ago.strftime('%B %d, %Y')} - {today.strftime('%B %d, %Y')}"
    }
    
    return render(request, 'core_pages/admin/analytics.html', context)