from nturl2path import url2pathname
from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('',views.index,name='home'),
    path('featured/', views.featured, name='featured'),
]
