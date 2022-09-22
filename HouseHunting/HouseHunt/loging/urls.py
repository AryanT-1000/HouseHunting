from django.urls import path

from loging import views

app_name = 'login'

urlpatterns = [
    path('', views.LoginFormView.as_view(), name="LoginForm"),
    path('login/', views.login_user, name='login_user'),
    # path('thanks/', views.rev, name='thanks_page'),
]
