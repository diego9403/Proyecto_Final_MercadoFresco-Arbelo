from django.urls import path
from MercadoFresco import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.cliente, name="Clientes"),
    path('tiendas/', views.tienda, name="Tiendas"),
    path('pedidos/', views.pedido, name="Pedidos"),
    path('busqueda/', views.busqueda, name="Busqueda"),
    path('buscarcliente/', views.buscarcliente),
    path('buscartienda/', views.buscartienda),
    path('buscarpedido/', views.buscarpedido),
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='MercadoFresco/logout.html'), name='Logout'),
    path('registro', views.register, name='Register'),
    path('perfil', views.perfil, name='Perfil'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('cliente/list', views.ClienteList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.ClienteDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.ClienteCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='Delete'),
    path('tienda/list', views.TiendaList.as_view(), name='ListT'),
    path(r'T^(?P<pk>\d+)$', views.TiendaDetalle.as_view(), name='DetailT'),
    path(r'T^nuevo$', views.TiendaCreacion.as_view(), name='NewT'),
    path(r'T^editar/(?P<pk>\d+)$', views.TiendaUpdate.as_view(), name='EditT'),
    path(r'T^borrar/(?P<pk>\d+)$', views.TiendaDelete.as_view(), name='DeleteT'),
    path('pedido/list', views.PedidoList.as_view(), name='ListP'),
    path(r'P^(?P<pk>\d+)$', views.PedidoDetalle.as_view(), name='DetailP'),
    path(r'P^nuevo$', views.PedidoCreacion.as_view(), name='NewP'),
    path(r'P^editar/(?P<pk>\d+)$', views.PedidoUpdate.as_view(), name='EditP'),
    path(r'P^borrar/(?P<pk>\d+)$', views.PedidoDelete.as_view(), name='DeleteP'),
    path('sobremi', views.sobre_mi, name='SobreMi')

]