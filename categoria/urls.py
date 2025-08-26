from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='categoria_index'),
    path('<int:categoria_id>/', views.detail, name='categoria_detail'),
    path('create/', views.create, name='categoria_create'),
    path('edit/<int:categoria_id>/', views.edit, name='categoria_edit'),
    path('delete/<int:categoria_id>/', views.delete, name='categoria_delete'),
]