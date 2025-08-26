from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('produto/', include('produto.urls')),
    path('estabelecimento/', include('estabelecimento.urls')),
    path('pedido/', include('pedido.urls')),
    path('itempedido/', include('itempedido.urls')),
    path('categoria/', include('categoria.urls')),
    path('', views.home, name='home'),
]
