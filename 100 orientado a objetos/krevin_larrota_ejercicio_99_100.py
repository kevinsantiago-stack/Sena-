#ejemplo 99  funciones

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo")
curso = Curso()
curso.agregar_estudiante(kevin_santiago_larrota_cuervo)
print([e.nombre for e in curso.estudiantes])


#ejemplo 100  funciones

class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

kevin_santiago_larrota_cuervo = Estudiante()
kevin_santiago_larrota_cuervo.actividad()
