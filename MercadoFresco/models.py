from django.db import models

# Create your models here.


class Cliente(models.Model):
    
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    nro_tel=models.IntegerField(max_length=30)
    email=models.EmailField(max_length=60)
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}"


class Tienda(models.Model):

    nombre=models.CharField(max_length=30)
    nro_tel=models.IntegerField(max_length=30)
    email=models.EmailField(max_length=60)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return f"Tienda: {self.nombre}"



class Pedido(models.Model):

    cliente=models.CharField(max_length=30)
    tienda=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=500)
    
    

    def __str__(self):
        return f"Cliente: {self.cliente} Tienda:{self.tienda} Nro pedido:{self.id}"


 

        



