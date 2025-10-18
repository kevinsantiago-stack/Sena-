#ejemplo 23 funciones 

class Persona:
    especie = "Humano"
    def __init__(self, nombre):
        self.nombre = nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo.nombre, "-", Persona.especie)


# ejemplo 24 funciones 

class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

kevin_santiago_larrota_cuervo = Luz()
kevin_santiago_larrota_cuervo.cambiar_estado()
print(kevin_santiago_larrota_cuervo.encendida)

