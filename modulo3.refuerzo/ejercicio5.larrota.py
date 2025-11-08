class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    def devolver(self):
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar(self, libro):
        self.libros.append(libro)
    def listar(self):
        return self.libros

if __name__ == '__main__':
    b = Biblioteca()
    l1 = Libro('1984', 'Orwell', 1949)
    b.agregar(l1)
    print([(x.titulo, x.prestado) for x in b.listar()])
    print('Prestar:', l1.prestar())
    print('Estado:', l1.prestado)
