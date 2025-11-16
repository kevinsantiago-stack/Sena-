

class Auto:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False

kevin_santiago_larrota_cuervo = Auto("Toyota")
kevin_santiago_larrota_cuervo.encender()
print(kevin_santiago_larrota_cuervo.encendido)




class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
    def ganar_partido(self):
        self.puntos += 3

kevin_santiago_larrota_cuervo = Equipo("Kevin Santiago Larrota Cuervo FC")
kevin_santiago_larrota_cuervo.ganar_partido()
print(kevin_santiago_larrota_cuervo.puntos)