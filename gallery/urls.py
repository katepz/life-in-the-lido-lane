from . import views
from django.urls import path

urlpatterns = [
    path('', views.gallery_page, name='gallery'),
]