class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def vender(self, cantidad):
        if cantidad<=self.stock:
            self.stock -= cantidad
            return True
        return False

class Inventario:
    def __init__(self):
        self.productos = []
    def agregar(self,p): self.productos.append(p)
    def buscar(self,nombre): return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

if __name__ == "__main__":
    p = Producto('Lapicero', 0.5, 10)
    inv = Inventario()
    inv.agregar(p)
    print(inv.buscar('lapi')[0].stock)
