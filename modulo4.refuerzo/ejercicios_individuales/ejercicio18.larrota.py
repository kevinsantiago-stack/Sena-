# Ejercicio 18: pagination view
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post
def lista_posts(request):
    qs = Post.objects.filter(publicado=True).order_by('-creado')
    paginator = Paginator(qs, 5)
    page = request.GET.get('page', 1)
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})
