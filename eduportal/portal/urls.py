from django.urls import path

from portal import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('info/<slug:info_slug>/', views.show_info, name='show_info'),
]