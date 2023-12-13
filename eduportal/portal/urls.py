from django.urls import path

from portal import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('infoforenrollee/', views.infoforenrollee, name='infoforenrollee'),
    path('infoforstudents/', views.infoforstudents, name='infoforstudents'),
    path('ourprojects/', views.our_projects, name='ourprojects'),
    path('science/', views.science, name='science'),
    path('schedule/', views.schedule, name='schedule'),
    path('psychology/', views.psychology, name='psychology'),
    path('sdo/', views.sdo, name='sdo'),

]