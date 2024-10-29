from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'goal_title', 'description', 'due_date', 'progress_percentage', 'created_at', 'updated_at')
    search_fields = ('goal_title',)

admin.site.register(Goal, GoalAdmin)