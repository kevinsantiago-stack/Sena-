class Vehiculo:
    def info(self):
        print("Soy un vehículo")

class Auto(Vehiculo):
    def info(self):
        print("Soy un auto")

kevin_santiago_larrota_cuervo = Auto()
kevin_santiago_larrota_cuervo.info()