
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado(Persona):
    def __init__(self, nombre, salario):
        super().__init__(nombre)
        self.salario = salario

kevin_santiago_larrota_cuervo = Empleado("Kevin Santiago Larrota Cuervo", 3000)
print(kevin_santiago_larrota_cuervo.nombre, kevin_santiago_larrota_cuervo.salario)
 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
nuevo_kevin = kevin_santiago_larrota_cuervo.duplicar()
print(nuevo_kevin.nombre)