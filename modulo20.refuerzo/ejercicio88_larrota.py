class Animal:
    def sonido(self):
        print("Hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau!")

kevin_santiago_larrota_cuervo = Perro()
kevin_santiago_larrota_cuervo.sonido()
