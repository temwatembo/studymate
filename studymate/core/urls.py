from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),  # Main page
    path('progress-report/', views.progress_report, name='progress_report'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('users/', views.users_list, name='users_list'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
]
