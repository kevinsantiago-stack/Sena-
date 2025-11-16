

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo")
matematicas = Curso()
matematicas.agregar_estudiante(kevin_santiago_larrota_cuervo)
print([e.nombre for e in matematicas.estudiantes])

