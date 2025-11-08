# Ejercicio 4: Vista simple
from django.http import HttpResponse
def hola(request):
    return HttpResponse('¡Hola, Django!')
