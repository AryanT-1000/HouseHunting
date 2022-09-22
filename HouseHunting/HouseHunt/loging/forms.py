from django import forms
from loging.models import TenentUser

# Define your forms here

class LoginForm(forms.ModelForm):
    class Meta:
        model = TenentUser
        fields = ['email', 'password']
