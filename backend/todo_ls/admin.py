from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TasksList)
class TasksListAdmin(admin.ModelAdmin):
    pass
