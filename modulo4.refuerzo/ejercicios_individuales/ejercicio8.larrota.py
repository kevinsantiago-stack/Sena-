# Ejercicio 8: Modelo Categoria
from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.nombre
