class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_amigo(self, nombre_amigo):
        return Persona(nombre_amigo)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
amigo = kevin_santiago_larrota_cuervo.crear_amigo("Juan")
print(amigo.nombre)