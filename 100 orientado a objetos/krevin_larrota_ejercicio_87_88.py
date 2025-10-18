#ejemplo 87  funciones

class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __gt__(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Coche", 120)
v2 = Vehiculo("Moto", 100)
kevin_santiago_larrota_cuervo = v1 > v2
print(kevin_santiago_larrota_cuervo)

#ejemplo 88  funciones

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
