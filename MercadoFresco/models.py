from django.db import models

# Create your models here.


class Cliente(models.Model):
    
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nro_tel=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}"


class Tienda(models.Model):

    nombre=models.CharField(max_length=50)
    nro_tel=models.IntegerField()
    email=models.EmailField()
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return f"Tienda: {self.nombre}"



class Pedido(models.Model):

    cliente=models.CharField(max_length=50)
    tienda=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=500)
    

    def __str__(self):
        return f"Cliente: {self.cliente} Tienda:{self.tienda}"


 

        



