from django.urls import path

from portal import views

urlpatterns = [
    path('', views.PortalHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('info/<slug:info_slug>/', views.show_info, name='show_info'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
]