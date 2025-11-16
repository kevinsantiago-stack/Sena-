

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return sum(self.notas) / len(self.notas)

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo", [80, 90, 70])
print(kevin_santiago_larrota_cuervo.promedio())


