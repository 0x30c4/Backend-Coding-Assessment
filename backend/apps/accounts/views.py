from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect

from apps.accounts.forms import LoginForm
from django.contrib.auth import logout


def logout_view(request):
    '''
    This is the logout view.
    '''
    logout(request)
    return redirect('accounts.login')


class LoginView(auth_views.LoginView):
    '''
    This is the simple login view.
    '''
    form_class = LoginForm
    template_name = 'accounts/login.html'
