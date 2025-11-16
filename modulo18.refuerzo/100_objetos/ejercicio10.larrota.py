

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

kevin_santiago_larrota_cuervo = Curso("Matemáticas")
kevin_santiago_larrota_cuervo.agregar_estudiante("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo.estudiantes)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
hijo = kevin_santiago_larrota_cuervo.crear_hijo()
print(hijo.nombre)