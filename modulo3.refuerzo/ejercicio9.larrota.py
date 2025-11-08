class Inventario:
    def __init__(self):
        self.armas = []
        self.pociones = []
    def agregar_arma(self, arma):
        self.armas.append(arma)
    def usar_pocion(self):
        if self.pociones:
            return self.pociones.pop()
        return None

if __name__ == '__main__':
    inv = Inventario()
    inv.armas.append('Espada')
    inv.pociones.append('Poción de Vida')
    print(inv.armas, inv.usar_pocion())
