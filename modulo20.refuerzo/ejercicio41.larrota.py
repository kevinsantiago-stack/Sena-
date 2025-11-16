
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

kevin_santiago_larrota_cuervo = Vehiculo("Moto", 80)
print(kevin_santiago_larrota_cuervo.obtener_velocidad())


