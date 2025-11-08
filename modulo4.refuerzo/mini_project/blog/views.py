from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.filter(publicado=True).order_by('-creado')[:10]
    return render(request, 'blog/home.html', {'posts': posts})

def saludo(request, nombre):
    from django.http import HttpResponse
    return HttpResponse(f'¡Hola, {nombre}!')

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post creado')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/crear_post.html', {'form': form})
