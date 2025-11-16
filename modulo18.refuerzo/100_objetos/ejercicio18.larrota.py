
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
print(f"{kevin_santiago_larrota_cuervo.nombre} tiene {kevin_santiago_larrota_cuervo.edad} años")



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
kevin_santiago_larrota_cuervo.cumplir_anos()
print(kevin_santiago_larrota_cuervo.edad)

