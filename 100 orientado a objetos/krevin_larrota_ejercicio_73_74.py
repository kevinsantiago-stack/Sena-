#ejemplo 73  funciones

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.estudiantes = []
    def agregar(self, estudiante):
        self.estudiantes.append(estudiante)
    def aprobados(self):
        return [e.nombre for e in self.estudiantes if e.nota >= 60]

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo", 75)
curso = Curso()
curso.agregar(kevin_santiago_larrota_cuervo)
print(curso.aprobados())

#ejemplo 74  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona}, soy {self.nombre}")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.saludar("Juan")
