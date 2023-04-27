from django.apps import AppConfig


class TodoLsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_ls'
    verbose_name = 'Список запланированных задач'
    verbose_name_plural = 'Списки запланированных задач'