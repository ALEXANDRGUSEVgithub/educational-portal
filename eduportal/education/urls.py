from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('personal-area/', views.PersonalArea.as_view(), name='personal-area')
]