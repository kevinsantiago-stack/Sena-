# Ejercicio 6: Render plantilla ejemplo
from django.shortcuts import render
def home(request):
    context = {'titulo':'Mi Blog','items':['Python','Django','Web']}
    return render(request, 'blog/home.html', context)
