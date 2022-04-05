from re import template
from django.shortcuts import render


def index(request):
    template = "posts/index.html"
    context = {
        'title': "Это главная страница проекта Yatube",
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = "posts/group_list.html"
    context = {
        'title': "Здесь будет информация о группах проекта Yatube",
    }
    return render(request, template, context)
