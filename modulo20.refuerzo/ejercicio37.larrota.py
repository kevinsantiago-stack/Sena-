

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} USD"

kevin_santiago_larrota_cuervo = Producto("Mouse", 25)
print(kevin_santiago_larrota_cuervo)



