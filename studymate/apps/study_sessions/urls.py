# apps/study_sessions/urls.py

from django.urls import path
from . import views

app_name = 'study_sessions'

urlpatterns = [
    path('', views.study_session_list, name='study_session_list'),
    path('create/', views.study_session_create, name='study_session_create'),
    path('update/<int:pk>/', views.study_session_update, name='study_session_update'),
    path('delete/<int:pk>/', views.study_session_delete, name='study_session_delete'),
]
