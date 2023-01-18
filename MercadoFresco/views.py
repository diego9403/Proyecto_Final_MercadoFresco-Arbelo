from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from MercadoFresco.models import Cliente,Tienda,Pedido


def inicio(request):

    return render(request, "MercadoFresco/inicio.html")


# Ingresar datos en la base de datos

from MercadoFresco.forms import ClienteFormulario, TiendaFormulario, PedidoFormulario
 
def cliente(request):
 
      if request.method == "POST":
 
            miFormulario = ClienteFormulario(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], nro_tel=informacion["nro_tel"],email=informacion["email"])
                  cliente.save()
                  return render(request, "MercadoFresco/inicio.html")
      else:
            miFormulario = ClienteFormulario()
 
      return render(request, "MercadoFresco/clientes.html", {"miFormulario": miFormulario})

def tienda(request):
     
      if request.method == "POST":
 
            miFormulario = TiendaFormulario(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  tienda = Tienda(nombre=informacion["nombre"], nro_tel=informacion["nro_tel"],email=informacion["email"], direccion=informacion["direccion"])
                  tienda.save()
                  return render(request, "MercadoFresco/inicio.html")
      else:
            miFormulario = TiendaFormulario()
 
      return render(request, "MercadoFresco/tiendas.html", {"miFormulario": miFormulario})


def pedido(request):
     
      if request.method == "POST":
 
            miFormulario = PedidoFormulario(request.POST) 
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  pedido = Pedido(cliente=informacion["cliente"], tienda=informacion["tienda"],descripcion=informacion["descripcion"])
                  pedido.save()
                  return render(request, "MercadoFresco/inicio.html")
      else:
            miFormulario = PedidoFormulario()
 
      return render(request, "MercadoFresco/pedidos.html", {"miFormulario": miFormulario})


#---------------------------------------------------------------------------------------------------------------------

#Busquedas en la base de datos


def busqueda(request):
    
      return render(request, "MercadoFresco/busqueda.html")


def buscarcliente(request):
    
      
      if  request.GET["nombre"]:
    
            nombre = request.GET["nombre"] 
            cliente = Cliente.objects.filter(nombre__icontains=nombre)
            
            return render(request, "MercadoFresco/resultadobusquedacliente.html", {"cliente":cliente, "nombre":nombre})
      
      else: 
        
            return render(request,"MercadoFresco/busquedafallo.html")


def buscartienda(request):
    
      
      if request.GET["nombre"]:
    
            nombre = request.GET["nombre"] 
            tienda = Tienda.objects.filter(nombre__icontains=nombre)

            return render(request, "MercadoFresco/resultadobusquedatienda.html", {"tienda":tienda, "nombre":nombre})
      else: 
        
            return  render(request,"MercadoFresco/busquedafallo.html")

def buscarpedido(request):
    
      
      if request.GET["id"]:
    
            id = request.GET["id"] 
            pedido = Pedido.objects.filter(id__icontains=id)

            return render(request, "MercadoFresco/resultadobusquedapedido.html", {"pedido":pedido,"id":id})
      else: 
        
            return render(request,"MercadoFresco/busquedafallo.html")

#-----------------------------------------------------------------------------------


         
