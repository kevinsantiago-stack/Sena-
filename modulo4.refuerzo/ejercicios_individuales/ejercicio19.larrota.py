# Ejercicio 19: search with Q
from django.db.models import Q
from django.shortcuts import render
from .models import Post
def buscar(request):
    q = request.GET.get('q','')
    resultados = Post.objects.filter(Q(titulo__icontains=q) | Q(cuerpo__icontains=q))
    return render(request, 'blog/buscar.html', {'resultados': resultados, 'q': q})
