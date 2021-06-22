from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    description = models.TextField()
    fecha_fabricacion = models.DateTimeField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Boleta(models.Model):
    numero_de_orden = models.IntegerField()
    valor = models.IntegerField()
    autorizacion_boleta = models.CharField(null=True,max_length=50)

class Despacho(models.Model):
    numero_de_orden = models.IntegerField()
    direccion = models.CharField( max_length=150)
    autorizacion_despacho = models.CharField(null = True,max_length=50)       

class Stock(models.Model):
    stock = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT, default=True)     