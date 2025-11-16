

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def listar_libros(self):
        return [l.titulo for l in self.libros]

kevin_santiago_larrota_cuervo = Libro("Python Básico")
mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(kevin_santiago_larrota_cuervo)
print(mi_biblioteca.listar_libros())


