
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

kevin_santiago_larrota_cuervo = Producto("Laptop", 1500)
mi_tienda = Tienda()
mi_tienda.agregar_producto(kevin_santiago_larrota_cuervo)
for p in mi_tienda.productos:
    print(p.nombre, p.precio)



class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

kevin_santiago_larrota_cuervo = Cuenta("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.depositar(500)
print(kevin_santiago_larrota_cuervo.saldo)