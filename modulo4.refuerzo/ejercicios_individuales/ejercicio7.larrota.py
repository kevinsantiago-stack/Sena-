# Ejercicio 7: Modelo Post
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.titulo
