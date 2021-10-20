from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, Image, Comments,Setting

from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    re_password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


# class SettingForm(forms.Form):
#     PROFILE_STATUS = (
#         ("public", "Public"),
#         ("private", "Private")
#     )
#
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     status = forms.CharField(max_length=10, widget=forms.Select(choices=PROFILE_STATUS))
