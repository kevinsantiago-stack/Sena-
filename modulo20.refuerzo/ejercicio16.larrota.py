

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

libro_kslc = Libro("Python Avanzado")
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro_kslc)
print([l.titulo for l in biblioteca.libros])


from abc import ABC, abstractmethod

