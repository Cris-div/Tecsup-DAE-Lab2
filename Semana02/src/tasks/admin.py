from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'priority', 'status', 'assigned_to', 'due_date', 'created_date')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_date'
