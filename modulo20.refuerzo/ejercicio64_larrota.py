class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __repr__(self):
        return f"Vehiculo('{self.tipo}', {self.velocidad})"

kevin_santiago_larrota_cuervo = Vehiculo("Bicicleta", 20)
print(repr(kevin_santiago_larrota_cuervo))