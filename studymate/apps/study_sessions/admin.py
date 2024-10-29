from django.contrib import admin

from .models import StudySession

class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time', 'subject', 'session_duration', 'created_at', 'updated_at')
    search_fields = ('subject',)

admin.site.register(StudySession, StudySessionAdmin)