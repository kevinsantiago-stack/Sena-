

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def info(self):
        print(f"Vehículo: {self.marca} {self.modelo}")

kevin_santiago_larrota_cuervo = Vehiculo("Toyota", "Corolla")
kevin_santiago_larrota_cuervo.info()




