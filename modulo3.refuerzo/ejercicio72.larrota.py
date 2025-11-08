class InventarioAvanzado:
    def __init__(self): self.items = {}
    def agregar(self, nombre, cantidad=1): self.items[nombre] = self.items.get(nombre,0) + cantidad
    def usar(self, nombre): 
        if self.items.get(nombre,0)>0:
            self.items[nombre]-=1; return True
        return False
if __name__ == '__main__':
    inv = InventarioAvanzado(); inv.agregar('Poción',3); print(inv.usar('Poción'), inv.items)
