from django.urls import path

from apps.gallery import views

urlpatterns = [
    path('', views.index, name='gallery.home'),
]
