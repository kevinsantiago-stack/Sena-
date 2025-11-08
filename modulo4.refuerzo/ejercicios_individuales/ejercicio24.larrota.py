# Ejercicio 24: crear superuser programaticamente (script)
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mi_sitio.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
def crear_superuser(username='admin', email='admin@example.com', password='admin123'):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
if __name__=='__main__': crear_superuser()
