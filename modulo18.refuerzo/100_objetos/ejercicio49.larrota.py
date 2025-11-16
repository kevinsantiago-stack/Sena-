
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



class Persona:
    def actividad(self):
        print("Realizando actividad")

class Estudiante(Persona):
    def actividad(self):
        print("Estudiando")

kevin_santiago_larrota_cuervo = Estudiante()
kevin_santiago_larrota_cuervo.actividad()
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
kevin_santiago_larrota_cuervo.cumplir_anos()
print(kevin_santiago_larrota_cuervo.edad)



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def es_mas_rapido_que(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Moto", 120)
v2 = Vehiculo("Coche", 100)
kevin_santiago_larrota_cuervo = v1.es_mas_rapido_que(v2)
print(kevin_santiago_larrota_cuervo)