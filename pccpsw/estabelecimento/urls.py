from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='estabelecimento_index'),
    path('<int:estabelecimento_id>/', views.detail, name='estabelecimento_detail'),
    path('create/', views.create, name='estabelecimento_create'),
    path('edit/<int:estabelecimento_id>/', views.edit, name='estabelecimento_edit'),
    path('delete/<int:estabelecimento_id>/', views.delete, name='estabelecimento_delete'),
]