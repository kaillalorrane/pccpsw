from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='itempedido_index'),
    path('<int:itempedido_id>/', views.detail, name='itempedido_detail'),
    path('create/', views.create, name='itempedido_create'),
    path('edit/<int:itempedido_id>/', views.edit, name='itempedido_edit'),
    path('delete/<int:itempedido_id>/', views.delete, name='itempedido_delete'),
    path('get-preco-produto/', views.get_preco_produto, name='get_preco_produto'),
]