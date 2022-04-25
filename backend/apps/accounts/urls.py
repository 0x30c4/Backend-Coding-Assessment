from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='accounts.login'),
]
