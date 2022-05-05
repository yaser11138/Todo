from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoApp(admin.ModelAdmin):
    fields = ("title", "user", "time", "date")

