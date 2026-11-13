from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    codigo_clasificacion = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} ({self.codigo_clasificacion})'


class Producto(models.Model):
    codigo_sku = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=120)
    marca = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    disponible = models.BooleanField(default=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='productos'
    )

    def __str__(self):
        return f'{self.codigo_sku} - {self.nombre} ({self.marca})'