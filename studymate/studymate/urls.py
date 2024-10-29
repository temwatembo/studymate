from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
    path('goals/', include('apps.goals.urls')),  
    path('study_sessions/', include('apps.study_sessions.urls')),  
    path('tasks/', include('apps.tasks.urls')),  
    path('reminders/', include('apps.reminders.urls')), 
]
