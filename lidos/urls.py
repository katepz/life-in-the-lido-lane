from . import views
from django.urls import path

urlpatterns = [
    path('', views.LidoList.as_view(), name = 'home'),
    path('<slug:slug>/', views.lido_detail, name='lido_detail'),
]