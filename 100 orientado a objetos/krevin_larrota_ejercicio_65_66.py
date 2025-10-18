#ejemplo 65  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo", "Ingeniería")
print(kevin_santiago_larrota_cuervo.nombre, kevin_santiago_larrota_cuervo.carrera)


#ejemplo 66  funciones

class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

kevin_santiago_larrota_cuervo = Cuenta("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.interes(5)
print(kevin_santiago_larrota_cuervo.saldo)
