from django.shortcuts import render
from loging.models import TenentUser
from django.views.generic.edit import FormView
from loging.forms import LoginForm

# Create your views here.

def index(request):
    return render(request, "loging/home.html",{})

def rev(request):
    return render(request, "loging/thanks.html",{})

class LoginFormView(FormView):
    template_name = 'loging/account.html' # 'loging/login.html'
    form_class = LoginForm
    # success_url = 'home1.html'

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = TenentUser.emp_auth.get(email=email, password=password)
            if user is not None:
                return render(request, 'thanks.html', {})
            else:
                print('Invalid user')
        except Exception as identifier:
            return render(request, 'loging/home.html')
    else:
        return render(request, 'loging/login.html')