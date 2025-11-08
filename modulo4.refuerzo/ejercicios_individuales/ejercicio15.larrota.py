# Ejercicio 15: management command skeleton
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Imprime saludo'
    def handle(self, *args, **options'):
        self.stdout.write('Hola comando')
