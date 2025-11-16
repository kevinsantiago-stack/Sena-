

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Restaurante:
    def __init__(self):
        self.menu = []

    def agregar_plato(self, plato):
        self.menu.append(plato)

kevin_santiago_larrota_cuervo = Plato("Pizza", 20)
mi_restaurante = Restaurante()
mi_restaurante.agregar_plato(kevin_santiago_larrota_cuervo)
for plato in mi_restaurante.menu:
    print(plato.nombre, plato.precio)




