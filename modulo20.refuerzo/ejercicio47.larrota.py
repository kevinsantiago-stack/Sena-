
class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("Stock insuficiente")

kevin_santiago_larrota_cuervo = Producto("Mouse", 10)
kevin_santiago_larrota_cuervo.vender(3)
print(kevin_santiago_larrota_cuervo.stock)




