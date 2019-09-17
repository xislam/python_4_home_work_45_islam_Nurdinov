from django.contrib import admin
from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status']
    list_filter = ['status']
    list_display_links = ['pk', 'description']
    search_fields = ['description', 'date']
    fields = ['description',  'date', 'status']


admin.site.register(Task, TaskAdmin)
