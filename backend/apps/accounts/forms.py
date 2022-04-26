from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

class LoginForm(AuthenticationForm):
    """
    This is the main login page
    """
    username = forms.CharField(label='Email / Username')
