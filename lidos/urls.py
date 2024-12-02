from . import views
from django.urls import path

urlpatterns = [
    path('', views.LidoList.as_view(), name = 'home'),
    path('<slug:slug>/', views.lido_detail, name='lido_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name = 'comment_edit'),
]