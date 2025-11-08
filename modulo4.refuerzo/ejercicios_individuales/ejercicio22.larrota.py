# Ejercicio 22: login view
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username'); password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user); messages.success(request, 'Bienvenido'); return redirect('home')
        messages.error(request, 'Credenciales inválidas')
    return render(request, 'blog/login.html')
