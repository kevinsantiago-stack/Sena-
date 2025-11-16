

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




