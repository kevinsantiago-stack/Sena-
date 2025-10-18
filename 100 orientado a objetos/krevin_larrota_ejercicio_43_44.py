#ejemplo 43  funciones

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def calcular_bono(self):
        return self.salario * 0.1

kevin_santiago_larrota_cuervo = Empleado("Kevin Santiago Larrota Cuervo", 3000)
print(kevin_santiago_larrota_cuervo.calcular_bono())


#ejemplo 44  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Alumno(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

kevin_santiago_larrota_cuervo = Alumno("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.estudiar()
