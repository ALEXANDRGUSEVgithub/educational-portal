from django.urls import path

from portal import views

urlpatterns = [
    path('', views.PortalHome.as_view(), name='home'),
    path('info/<slug:info_slug>/', views.ShowMainInfo.as_view(), name='show_info'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('addpage/', views.AddPage.as_view(), name='add_page')
]