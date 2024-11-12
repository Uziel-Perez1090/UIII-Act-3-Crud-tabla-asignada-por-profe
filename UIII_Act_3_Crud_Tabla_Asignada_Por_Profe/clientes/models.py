from django.db import models

# Create your models here.

class clientes(models.Model):
    id_clientes=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=8)
    apellido=models.CharField(max_length=8)
    telefono=models.CharField(max_length=8)
    email=models.CharField(max_length=8)
    direccion=models.CharField(max_length=8)
    comprobacion=models.CharField(max_length=8)
    id_productos=models.CharField(max_length=8)




    def __str__(self) :
        return self.nombre