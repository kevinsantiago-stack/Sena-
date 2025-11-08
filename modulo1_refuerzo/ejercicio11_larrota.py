# kevin santiago larrota cuervo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return f'{self.marca} {self.modelo}'

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

def main():
    c = Coche('Toyota', 'Corolla', 4)
    print(c)
    print('Puertas:', c.puertas)

if __name__ == '__main__':
    main()
