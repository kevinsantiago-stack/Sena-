
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

kevin_santiago_larrota_cuervo = Producto("Camisa", 50)
kevin_santiago_larrota_cuervo.aplicar_descuento(20)
print(kevin_santiago_larrota_cuervo.precio)


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

kevin_santiago_larrota_cuervo = CuentaBancaria("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.retirar(200)
print(kevin_santiago_larrota_cuervo.saldo)

