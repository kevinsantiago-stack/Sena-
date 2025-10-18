#ejemplo 95  funciones
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.tipo} a {self.velocidad} km/h"

kevin_santiago_larrota_cuervo = Vehiculo("Coche", 100)
print(kevin_santiago_larrota_cuervo)


#ejemplo 96  funciones

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def buscar(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return l
        return None

kevin_santiago_larrota_cuervo = Libro("Python Intermedio")
biblioteca = Biblioteca()
biblioteca.agregar_libro(kevin_santiago_larrota_cuervo)
print(biblioteca.buscar("Python Intermedio").titulo)
