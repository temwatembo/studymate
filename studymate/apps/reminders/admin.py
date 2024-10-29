from django.contrib import admin

from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('user', 'reminder_message', 'reminder_time', 'created_at', 'updated_at')
    search_fields = ('reminder_message',)

admin.site.register(Reminder, ReminderAdmin)