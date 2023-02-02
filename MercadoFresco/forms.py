from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    first_name=forms.CharField()
    last_name=forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','first_name','last_name']