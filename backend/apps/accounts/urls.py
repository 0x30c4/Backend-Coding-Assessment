from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='accounts.login'),
    path('logout', views.logout_view, name='accounts.logout'),
]
