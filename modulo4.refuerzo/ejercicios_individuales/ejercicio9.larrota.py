# Ejercicio 9: Registrar admin
from django.contrib import admin
from .models import Post, Categoria
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','creado')
admin.site.register(Categoria)
