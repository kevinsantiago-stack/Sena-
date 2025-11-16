
class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def obtener_velocidad(self):
        return self.velocidad

kevin_santiago_larrota_cuervo = Vehiculo("Moto", 80)
print(kevin_santiago_larrota_cuervo.obtener_velocidad())



class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

kevin_santiago_larrota_cuervo = Empleado("Kevin Santiago Larrota Cuervo", 3000)
kevin_santiago_larrota_cuervo.aumentar_salario(10)
print(kevin_santiago_larrota_cuervo.salario)