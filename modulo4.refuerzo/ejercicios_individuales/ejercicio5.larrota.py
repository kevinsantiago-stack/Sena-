# Ejercicio 5: Vista con parámetro
from django.http import HttpResponse
def saludo(request, nombre):
    return HttpResponse(f'¡Hola, {nombre}! Bienvenido a mi blog.')
