class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento

kevin_santiago_larrota_cuervo = Vehiculo("Coche", 50)
kevin_santiago_larrota_cuervo.acelerar(20)
print(kevin_santiago_larrota_cuervo.velocidad)