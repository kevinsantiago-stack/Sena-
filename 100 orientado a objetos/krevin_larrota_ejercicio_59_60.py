#ejemplo 59  funciones

class Vehiculo:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

kevin_santiago_larrota_cuervo = Vehiculo("Camión", 1000)
print(kevin_santiago_larrota_cuervo.tipo, kevin_santiago_larrota_cuervo.capacidad)


#ejemplo 60  funciones

class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

kevin_santiago_larrota_cuervo = Atleta("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.nadar()
kevin_santiago_larrota_cuervo.correr()
