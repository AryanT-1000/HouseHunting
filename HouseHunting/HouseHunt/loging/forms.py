from django import forms

from loging.models import TenentUser

# Define your forms here

class LoginForm(forms.Form):
    class Meta:
        model = TenentUser
        fields = ['email', 'password']
