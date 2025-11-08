# Ejercicio 11: crear_post view (uses PostForm)
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PostForm
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Post creado')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})
