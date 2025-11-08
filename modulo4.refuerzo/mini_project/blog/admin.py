from django.contrib import admin
from .models import Post, Categoria, Etiqueta

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','categoria','publicado','creado')
    search_fields = ('titulo','cuerpo')
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Categoria)
admin.site.register(Etiqueta)
