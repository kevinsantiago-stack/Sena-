#ejemplo 77  funciones

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

kevin_santiago_larrota_cuervo1 = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo2 = Persona("Juan")
print(Persona.contador)


#ejemplo 78  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_amigo(self, nombre_amigo):
        return Persona(nombre_amigo)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
amigo = kevin_santiago_larrota_cuervo.crear_amigo("Juan")
print(amigo.nombre)
