from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

posts = [
    {'id': 1, 'name': 'Новость номер 1', 'content': 'Какие то новости', 'is_published': True},
    {'id': 2, 'name': 'Новость номер 2', 'content': 'Какие то новости', 'is_published': True},
    {'id': 3, 'name': 'Статья', 'content': 'Какая то статья', 'is_published': True},
    {'id': 4, 'name': 'Новость номер 3', 'content': 'Какие то новости', 'is_published': True},
    {'id': 5, 'name': 'Новость номер 5', 'content': 'Какие то новости', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная станица',
        'posts': posts,
    }
    return render(request, 'portal/index.html', context=data)


def about(request):
    return render(request, 'portal/about.html', context={'title': 'О нас'})


def login(request):
    return HttpResponse('Войти')


def infoforenrollee(request):
    return HttpResponse('Информация поступающим')


def infoforstudents(request):
    return HttpResponse('Информация студентам')


def science(request):
    return HttpResponse('Наука')


def our_projects(request):
    return HttpResponse('Наши проекты')


def schedule(request):
    return HttpResponse('Расписание')


def psychology(request):
    return HttpResponse('Психологическая помощь')


def sdo(request):
    return HttpResponse('СДО')


