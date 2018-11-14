from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('main/', views.main, name='main'),
    re_path('makeTransaction/', views.makeTransaction),
    re_path('replenish/', views.replenish),
    ]