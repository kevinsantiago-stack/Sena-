class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Cuadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado
    def area(self):
        return self.lado ** 2

kevin_santiago_larrota_cuervo = Cuadrado(5)
print(kevin_santiago_larrota_cuervo.area())




