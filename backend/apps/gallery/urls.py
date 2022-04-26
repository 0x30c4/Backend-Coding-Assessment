from django.urls import path

from apps.gallery import views

urlpatterns = [
    path('items/', views.ItemsViewList.as_view(), name='gallery.home'),
    path('items/<int:pk>/', views.ItemsViewDetail.as_view(), name='gallery.items'),
]
