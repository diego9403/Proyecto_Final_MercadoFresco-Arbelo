from django.urls import path
from MercadoFresco import views



urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.cliente, name="Clientes"),
    path('tiendas/', views.tienda, name="Tiendas"),
    path('pedidos/', views.pedido, name="Pedidos"),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('buscarcliente/', views.buscarcliente),
    path('buscartienda/', views.buscartienda),
    path('buscarpedido/', views.buscarpedido,)
]