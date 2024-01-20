from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('personal-area/', views.PersonalArea.as_view(), name='personal-area'),
    path('course/<slug:course_slug>/', views.ShowCourse.as_view(), name='course'),
    path('my_group/', views.MuGroup.as_view(), name='my_group'),

    path('for_teacher/', views.teacher, name='for_teacher'),
    path('for_students/', views.students, name='for_students'),
    path('tests/', views.tests, name='tests'),
    path('library/', views.library, name='library')
]