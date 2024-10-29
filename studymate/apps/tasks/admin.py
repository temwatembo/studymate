from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_title', 'due_date', 'description', 'priority_level', 'status', 'created_at', 'updated_at')
    search_fields = ('task_title',)

admin.site.register(Task, TaskAdmin)