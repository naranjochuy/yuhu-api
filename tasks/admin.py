from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "email",
        "expiration_date"
    ]
    search_fields = [
        "title",
        "description",
        "email",
    ]
