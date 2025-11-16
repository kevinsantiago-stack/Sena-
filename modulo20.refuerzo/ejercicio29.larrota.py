

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.estudiar()


