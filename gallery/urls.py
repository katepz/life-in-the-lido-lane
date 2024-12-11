from . import views
from django.urls import path

urlpatterns = [
    path('update-photo/<int:pk>/', views.update_photo, name='update_photo'),
    path('delete-photo/<int:pk>/', views.delete_photo, name='delete_photo'),
    path('', views.gallery_page, name='gallery'),
]