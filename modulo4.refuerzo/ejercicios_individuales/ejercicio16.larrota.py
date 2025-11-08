# Ejercicio 16: DRF serializer (requires DRF)
from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','titulo','cuerpo','autor','creado']
