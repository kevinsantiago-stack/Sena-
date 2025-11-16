

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} USD"

kevin_santiago_larrota_cuervo = Producto("Mouse", 25)
print(kevin_santiago_larrota_cuervo)



class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def __repr__(self):
        return f"Vehiculo('{self.tipo}', {self.velocidad})"

kevin_santiago_larrota_cuervo = Vehiculo("Bicicleta", 20)
print(repr(kevin_santiago_larrota_cuervo))