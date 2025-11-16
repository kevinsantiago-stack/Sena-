class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

kevin_santiago_larrota_cuervo = Alumno("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.estudiar()