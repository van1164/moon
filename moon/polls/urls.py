from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.login, name = 'login'),
    path('finish', views.finish, name ='finish'),
    path('check', views.check, name ='check'),
    path('logout', views.logout, name ='logout'),
    path('login_re', views.login_re, name ='login_re'),
    path('login_re2', views.login_re2, name ='login_re2'),
    path('login_admin', views.login_admin, name ='login_admin'),
    path('xd', views.login_admin, name ='login_admin'),
    path('div', views.div, name ='div'),
    path('check_solo', views.check_solo, name ='check_solo'),
    path('submit', views.submit, name = "submit")
]