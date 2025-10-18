#ejemplo 33 funciones 

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

#ejemplo 34 funciones 

class Persona:
    pass

kevin_santiago_larrota_cuervo = Persona()
kevin_santiago_larrota_cuervo.nombre = "Kevin Santiago Larrota Cuervo"
print(kevin_santiago_larrota_cuervo.nombre)
