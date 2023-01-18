from django import forms

class ClienteFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    nro_tel=forms.IntegerField()
    email=forms.EmailField()

class TiendaFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=50)
    nro_tel=forms.IntegerField()
    email=forms.EmailField()
    direccion=forms.CharField(max_length=50)

class PedidoFormulario(forms.Form):
    
    cliente=forms.CharField(max_length=50)
    tienda=forms.CharField(max_length=50)
    descripcion=forms.CharField(max_length=500)

