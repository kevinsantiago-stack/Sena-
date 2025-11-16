

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.nombre = "Kevin Cuervo"
print(kevin_santiago_larrota_cuervo.nombre)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        return self.edad >= 18

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
print(kevin_santiago_larrota_cuervo.es_mayor())