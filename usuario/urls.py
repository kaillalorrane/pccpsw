from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:usuario_id>/', views.detail, name='usuario_detail'),
    path('create/', views.create, name='usuario_create'),
    path('edit/<int:usuario_id>/edit/', views.edit, name='usuario_edit'),
    path('delete/<int:usuario_id>/delete/', views.delete, name='usuario_delete'),
]