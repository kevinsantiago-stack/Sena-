
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __str__(self):
        return f"{self.tipo} a {self.velocidad} km/h"

kevin_santiago_larrota_cuervo = Vehiculo("Coche", 100)
print(kevin_santiago_larrota_cuervo)



