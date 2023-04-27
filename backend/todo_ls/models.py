from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    custom user
    """
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'


class Task(models.Model):
    """
    scheduled task
    """
    text = models.TextField(verbose_name='Задача')
    is_check = models.BooleanField(verbose_name='Выполнено', default=False)
    date_create = models.DateTimeField(verbose_name='date_create', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-date_create']

    def __str__(self):
        return self.text[:15] + '...' if len(self.text) > 32 else self.text


class TasksList(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=32)
    tasks = models.ManyToManyField(Task, verbose_name='Задачи')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    date_create = models.DateTimeField(verbose_name='date_create', auto_now_add=True)

    class Meta:
        verbose_name = 'Список задач'
        verbose_name_plural = 'Списки задач'
        ordering = ['-date_create']

    def __str__(self):
        return self.title
