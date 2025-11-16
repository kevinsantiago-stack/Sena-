
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        return self.edad >= 18

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
print(kevin_santiago_larrota_cuervo.es_mayor())