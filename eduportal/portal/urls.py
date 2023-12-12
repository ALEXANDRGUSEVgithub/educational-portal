from django.urls import path

from portal import views

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('about/', views.about, name='about'),
    path('login/', views.about, name='login'),
    path('contact/', views.contact, name='contact'),
]