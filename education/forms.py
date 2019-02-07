from django import forms

from django.contrib.auth.models import User
from django.forms import PasswordInput


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    age = forms.IntegerField()
    area = forms.CharField()
    role = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password','age','area','role']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']
