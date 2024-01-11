from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from users.models import User


# Create your views here.


# views.py

from django.shortcuts import render

def main(request):
    # Получаем профиль пользователя
    user = request.user
    print(user)
    # Если у пользователя есть группа, получаем курсы этой группы
    if user.group_stud:
        user_courses = user.group_stud.courses.all()
    else:
        user_courses = None

    return render(request, 'education/personal_area.html', {'user_courses': user_courses})


class PersonalArea(ListView):
    model = User
    template_name = 'education/personal_area.html'
    context_object_name = 'user_courses'

    extra_context = {
        'title': 'Личный кабинет'
    }

    def get_queryset(self):
        user = self.request.user

        if user.group_stud:
            return user.group_stud.courses.all()
        else:
            return None