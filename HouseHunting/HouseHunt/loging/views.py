from django.http import HttpResponse
from loging.forms import LoginForm
# from loging.models import TenentUser
from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.edit import FormView

# Create your views here.

class UserCreateView(CreateView): 
    pass

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UserLoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = 'thanks.html'

    def form_valid(self, form):
        return super().form_valid()

def home(request):
    return render(request,'home.html',{})
    
def account(request):
    return render(request,'account.html')
