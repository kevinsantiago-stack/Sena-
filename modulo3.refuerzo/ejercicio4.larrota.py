class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometros = 0
    def acelerar(self, km_recorridos):
        if km_recorridos > 0:
            self.kilometros += km_recorridos
            print(f"El {self.marca} {self.modelo} recorrió {km_recorridos} km")
        else:
            print("Los kilómetros deben ser positivos")
    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo} ({self.año})")
        print(f"Kilómetros recorridos: {self.kilometros} km")

if __name__ == '__main__':
    mi_auto = Auto('Toyota', 'Corolla', 2020)
    mi_auto.mostrar_info()
    mi_auto.acelerar(150)
    mi_auto.acelerar(75)
    mi_auto.mostrar_info()
