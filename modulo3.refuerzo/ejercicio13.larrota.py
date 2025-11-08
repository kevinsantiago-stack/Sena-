class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre; self.puesto = puesto; self.salario = salario
    def aumentar(self, pc): self.salario *= 1 + pc/100

if __name__ == '__main__':
    e = Empleado('Rosa','Dev',1000); e.aumentar(10); print(e.salario)
