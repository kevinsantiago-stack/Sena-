# Ejercicio 23: login_required view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def perfil(request):
    return render(request, 'blog/perfil.html', {'user': request.user})
