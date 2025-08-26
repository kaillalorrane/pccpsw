from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pedido_index'),
    path('<int:pedido_id>/', views.detail, name='pedido_detail'),
    path('create/', views.create, name='pedido_create'),
    path('edit/<int:pedido_id>/', views.edit, name='pedido_edit'),
    path('delete/<int:pedido_id>/', views.delete, name='pedido_delete'),
]