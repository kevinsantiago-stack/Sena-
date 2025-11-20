from rest_framework import serializers
from .models import beneficio

class beneficioSerializer(serializers.ModelSerializer):
    class Meta:
        model = beneficio
        fields = '__all__'