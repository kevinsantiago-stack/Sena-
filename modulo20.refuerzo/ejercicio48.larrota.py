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