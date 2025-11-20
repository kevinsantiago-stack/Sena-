from rest_framework import generics
from .models import beneficio
from .serializers import beneficioSerializer
from django.shortcuts import render

def inicio(request):
    beneficios = beneficio.objects.all()
    return render(request, 'beneficio/inicio.html', {'beneficios': beneficios})


class beneficioListCreateView(generics.ListCreateAPIView):
    queryset = beneficio.objects.all()
    serializer_class = beneficioSerializer

class beneficioRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = beneficio.objects.all()
    serializer_class = beneficioSerializer

