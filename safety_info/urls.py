from . import views
from django.urls import path

urlpatterns = [
    path('', views.safety_info, name='safety'),
]