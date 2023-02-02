from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from MercadoFresco.models import Cliente,Tienda,Pedido
from django.contrib.auth.decorators import login_required
from MercadoFresco.forms import ClienteFormulario, TiendaFormulario, PedidoFormulario, UserRegisterForm,UserEditForm




def inicio(request):
    
    return render(request, "MercadoFresco/inicio.html")



def register(request):
    
      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"MercadoFresco/inicio.html" ,  {"mensaje":"El Usuario ha sido Creado "})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"MercadoFresco/registro.html" ,  {"form":form})


 
@login_required
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

@login_required
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

@login_required
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

@login_required
def busqueda(request):
    
      return render(request, "MercadoFresco/busqueda.html")

@login_required
def buscarcliente(request):
    
      
      if  request.GET["nombre"]:
    
            nombre = request.GET["nombre"] 
            cliente = Cliente.objects.filter(nombre__icontains=nombre)
            
            return render(request, "MercadoFresco/resultadobusquedacliente.html", {"cliente":cliente, "nombre":nombre})
      
      else: 
        
            return render(request,"MercadoFresco/busquedafallo.html")

@login_required
def buscartienda(request):
    
      
      if request.GET["nombre"]:
    
            nombre = request.GET["nombre"] 
            tienda = Tienda.objects.filter(nombre__icontains=nombre)

            return render(request, "MercadoFresco/resultadobusquedatienda.html", {"tienda":tienda, "nombre":nombre})
      else: 
        
            return  render(request,"MercadoFresco/busquedafallo.html")

@login_required
def buscarpedido(request):
    
      
      if request.GET["id"]:
    
            id = request.GET["id"] 
            pedido = Pedido.objects.filter(id__icontains=id)

            return render(request, "MercadoFresco/resultadobusquedapedido.html", {"pedido":pedido,"id":id})
      else: 
        
            return render(request,"MercadoFresco/busquedafallo.html")

#-----------------------------------------------------------------------------------


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "MercadoFresco/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "MercadoFresco/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "MercadoFresco/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "MercadoFresco/login.html", {"form": form})



@login_required
def perfil(request):

      return render(request, "MercadoFresco/perfil.html")




@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            

            usuario.save()

            return render(request, "MercadoFresco/inicio.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "MercadoFresco/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#Crud cliente

class ClienteList(ListView):
    
    model = Cliente
    template_name = "MercadoFresco/cliente_list.html"

class ClienteDetalle(DetailView):

    model = Cliente
    template_name = "MercadoFresco/cliente_detalle.html"

class ClienteCreacion(CreateView):

    model = Cliente
    success_url = "/MercadoFresco/cliente/list"
    fields = ['nombre', 'apellido', 'nro_tel','email']

class ClienteUpdate(UpdateView):

      model = Cliente
      success_url = "/MercadoFresco/cliente/list"
      fields = ['nombre', 'apellido', 'nro_tel','email']

class ClienteDelete(DeleteView):

    model = Cliente
    success_url = "/MercadoFresco/cliente/list"




# Crud tienda

class TiendaList(ListView):
    
    model = Tienda
    template_name = "MercadoFresco/tienda_list.html"

class TiendaDetalle(DetailView):

    model = Tienda
    template_name = "MercadoFresco/tienda_detalle.html"

class TiendaCreacion(CreateView):

    model = Tienda
    success_url = "/MercadoFresco/tienda/list"
    fields = ['nombre','nro_tel','email','direccion']

class TiendaUpdate(UpdateView):

      model = Tienda
      success_url = "/MercadoFresco/tienda/list"
      fields = ['nombre','nro_tel','email','direccion']

class TiendaDelete(DeleteView):

    model = Tienda
    success_url = "/MercadoFresco/tienda/list"



#Crud pedidos


class PedidoList(ListView):
    
    model = Pedido
    template_name = "MercadoFresco/pedido_list.html"

class PedidoDetalle(DetailView):

    model = Pedido
    template_name = "MercadoFresco/pedido_detalle.html"
    

class PedidoCreacion(CreateView):

      model = Pedido
      success_url = "/MercadoFresco/pedido/list"
      fields = ['cliente','tienda','descripcion']   


class PedidoUpdate(UpdateView):

      model = Pedido
      success_url = "/MercadoFresco/pedido/list"
      fields = ['cliente','tienda','descripcion']

class PedidoDelete(DeleteView):

    model = Pedido
    success_url = "/MercadoFresco/pedido/list"



def sobre_mi(request):

      return render(request, "MercadoFresco/sobre_mi.html")