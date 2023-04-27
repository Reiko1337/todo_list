from django.shortcuts import render
from django.views.generic import TemplateView


class TodoView(TemplateView):
    template_name = 'todo.html'
