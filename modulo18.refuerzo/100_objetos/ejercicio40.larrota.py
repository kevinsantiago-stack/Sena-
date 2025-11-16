
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    @property
    def nombre(self):
        return self._nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo.nombre)



class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

resultado = Calculadora.sumar(10, 15)
print(resultado)