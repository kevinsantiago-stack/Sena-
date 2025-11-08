# Ejercicio 26: cache per-view example
from django.core.cache import cache
from django.shortcuts import render
from .models import Post
def cached_posts(request):
    posts = cache.get('posts_list')
    if posts is None:
        posts = list(Post.objects.filter(publicado=True).order_by('-creado')[:10])
        cache.set('posts_list', posts, 60)
    return render(request, 'blog/post_list.html', {'posts': posts})
