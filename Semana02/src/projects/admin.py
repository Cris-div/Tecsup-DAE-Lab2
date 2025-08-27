from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'start_date', 'end_date', 'created_at')
    search_fields = ('name', 'description', 'owner__username')
    list_filter = ('start_date',)
