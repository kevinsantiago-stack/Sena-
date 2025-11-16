class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
juan = Persona("Juan")
kevin_santiago_larrota_cuervo.agregar_amigo(juan)
print([a.nombre for a in kevin_santiago_larrota_cuervo.amigos])