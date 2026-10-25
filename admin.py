from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'department', 'employee', 'issue_date', 'get_cost', 'get_excerpt')


admin.site.register(Task, TaskAdmin)
