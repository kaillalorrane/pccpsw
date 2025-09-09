from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='produto_index'),
    path('<int:produto_id>/', views.detail, name='produto_detail'),
    path('create/', views.create, name='produto_create'),
    path('edit/<int:produto_id>/', views.edit, name='produto_edit'),
    path('delete/<int:produto_id>/', views.delete, name='produto_delete'),
]