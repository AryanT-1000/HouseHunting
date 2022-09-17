from django.contrib import admin
from django.urls import path
from loging import views

from loging.views import UserLoginView


urlpatterns = [path('login',UserLoginView.as_view(), name='UserLoginView'),
               path('home',views.home, name='home'),
               path('account',views.account, name='account'),]