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