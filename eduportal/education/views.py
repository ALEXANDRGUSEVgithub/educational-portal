from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from education.models import Courses
from users.models import GroupStudents


# Класс для отображения личного кабинета пользователя
class PersonalArea(ListView):
    model = Courses
    template_name = 'education/personal_area.html'
    context_object_name = 'courses'

    def get_queryset(self):
        # cat_user_id = 1 - Категория студенты
        # cat_user_id = 2 - Категория преподаватели

        # Проверка к какой категории относится пользователь. Возвращение данных из бд, в зависимости к какой группе
        # относится пользователь
        user = self.request.user
        if user.cat_user_id == 1:
            if user.group_stud:
                return user.group_stud.courses.all()
            else:
                return None
        elif user.cat_user_id == 2:
            return user.courses.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['title'] = 'Ваши курсы'
        return context


# Класс для отображения курса
class ShowCourse(DetailView):
    model = Courses
    template_name = 'education/course.html'
    slug_url_kwarg = 'course_slug'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['course']
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Courses, slug=self.kwargs[self.slug_url_kwarg])


# Класс для отображения страницы с пользователями, относящимися к одной группе
class MuGroup(ListView):
    model = GroupStudents
    template_name = 'education/my_group_stud.html'
    context_object_name = 'my_group'

    def get_queryset(self):
        user = self.request.user

        # Проверка находится ли пользователь в какой-либо группе
        if user.group_stud:
            return user.group_stud
        else:
            return None


# Функции заглушки
def teacher(request):
    return HttpResponse("Для преподавателей")


def students(request):
    return HttpResponse("Для преподавателей")


def tests(request):
    return HttpResponse("Тесты")


def library(request):
    return HttpResponse("Библиотека")
