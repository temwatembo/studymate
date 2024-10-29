# apps/reminders/urls.py

from django.urls import path
from . import views

app_name = 'reminders'

urlpatterns = [
    path('', views.reminder_list, name='reminder_list'),
    path('create/', views.reminder_create, name='reminder_create'),
    path('update/<int:pk>/', views.reminder_update, name='reminder_update'),
    path('delete/<int:pk>/', views.reminder_delete, name='reminder_delete'),
]
