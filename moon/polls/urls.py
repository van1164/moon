from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.home, name = 'home'),
    path('finish', views.finish, name ='finish'),
    path('check', views.check, name ='check')

]