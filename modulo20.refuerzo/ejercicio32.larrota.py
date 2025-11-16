

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo", "Ingeniería")
print(kevin_santiago_larrota_cuervo.nombre, kevin_santiago_larrota_cuervo.carrera)


