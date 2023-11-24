from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns = [
path('', index,name='index'),
path('signup/',signup,name='signup'),
path('login/',login,name='login'),
path('register/',register,name='register'),
path('rec/',rec,name='rec')

]
