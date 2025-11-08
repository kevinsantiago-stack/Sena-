# Ejercicio 12: urls app
from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('post/nuevo/', views.crear_post, name='post_create'),
    path('saludo/<str:nombre>/', views.saludo, name='saludo'),
]
