class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def info(self):
        return f"{self.marca} {self.modelo}"

class Auto(Vehiculo):
    def acelerar(self):
        return "Acelerando..."

class Moto(Vehiculo):
    def hacer_caballito(self):
        return "Hace caballito!"

if __name__ == "__main__":
    a = Auto('Toyota','Corolla')
    print(a.info(), a.acelerar())
