

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

kevin_santiago_larrota_cuervo = Curso("Matemáticas")
kevin_santiago_larrota_cuervo.agregar_estudiante("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo.estudiantes)



