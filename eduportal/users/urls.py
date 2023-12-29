from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
]