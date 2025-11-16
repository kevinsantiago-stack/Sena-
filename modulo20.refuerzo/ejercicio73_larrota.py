class Pedido:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def total(self):
        return sum(p.precio for p in self.productos)

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

kevin_santiago_larrota_cuervo = Producto("Libro", 30)
pedido = Pedido()
pedido.agregar_producto(kevin_santiago_larrota_cuervo)
print(pedido.total())