
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

kevin_santiago_larrota_cuervo = Empleado("Kevin Santiago Larrota Cuervo", 3000)
print(kevin_santiago_larrota_cuervo.nombre, kevin_santiago_larrota_cuervo.salario)
 

