class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def filtrar_por_autor(self, autor):
        return [l.titulo for l in self.libros if l.autor == autor]

kevin_santiago_larrota_cuervo = Libro("Python Avanzado", "Kevin Santiago Larrota Cuervo")
biblioteca = Biblioteca()
biblioteca.agregar_libro(kevin_santiago_larrota_cuervo)
print(biblioteca.filtrar_por_autor("Kevin Santiago Larrota Cuervo"))