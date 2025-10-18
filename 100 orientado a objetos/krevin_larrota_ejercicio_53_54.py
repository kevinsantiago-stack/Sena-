#ejemplo 53  funciones

class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

kevin_santiago_larrota_cuervo = Cuadrado(5)
print(kevin_santiago_larrota_cuervo.area())


#ejemplo 54  funciones

class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

kevin_santiago_larrota_cuervo = Profesor("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.agregar_materia("Matemáticas")
print(kevin_santiago_larrota_cuervo.materias)
