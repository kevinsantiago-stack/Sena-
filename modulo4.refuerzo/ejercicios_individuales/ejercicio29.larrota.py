# Ejercicio 29: sitemap example
from django.contrib.sitemaps import Sitemap
from .models import Post
class PostSitemap(Sitemap):
    changefreq = 'daily'; priority = 0.8
    def items(self): return Post.objects.filter(publicado=True)
    def lastmod(self,obj): return obj.creado
