# Ejercicio 20: Modelo Perfil con ImageField
from django.db import models
class Perfil(models.Model):
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
