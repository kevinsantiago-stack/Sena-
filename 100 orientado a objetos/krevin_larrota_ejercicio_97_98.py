#ejemplo 97  funciones

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anos(self):
        self.edad += 1

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
kevin_santiago_larrota_cuervo.cumplir_anos()
print(kevin_santiago_larrota_cuervo.edad)

#ejemplo 98  funciones

class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def es_mas_rapido_que(self, otro):
        return self.velocidad > otro.velocidad

v1 = Vehiculo("Moto", 120)
v2 = Vehiculo("Coche", 100)
kevin_santiago_larrota_cuervo = v1.es_mas_rapido_que(v2)
print(kevin_santiago_larrota_cuervo)
