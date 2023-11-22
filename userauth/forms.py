from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauth.models import User
from .models import Email


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['address']


class ProfileForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)