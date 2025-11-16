 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

kevin_santiago_larrota_cuervo = Banco("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.mostrar_saldo()




class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

kevin_santiago_larrota_cuervo = Gerente("Kevin Santiago Larrota Cuervo", 5000, "Ventas")
print(kevin_santiago_larrota_cuervo.nombre, kevin_santiago_larrota_cuervo.departamento)