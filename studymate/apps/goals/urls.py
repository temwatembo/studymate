# apps/goals/urls.py

from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('create/', views.goal_create, name='goal_create'),
    path('update/<int:pk>/', views.goal_update, name='goal_update'),
    path('delete/<int:pk>/', views.goal_delete, name='goal_delete'),
]
