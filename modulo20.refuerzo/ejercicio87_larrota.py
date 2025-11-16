

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)

    def set_edad(self, edad):
        if edad < 0:
            self.edad = 0
        else:
            self.edad = edad

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", -5)
print(kevin_santiago_larrota_cuervo.edad)