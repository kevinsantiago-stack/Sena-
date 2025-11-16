

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo.nombre)



class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy {self.nombre}")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.saludar()



