
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



