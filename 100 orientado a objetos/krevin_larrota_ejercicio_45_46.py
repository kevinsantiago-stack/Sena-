#ejemplo 45  funciones

class Persona:
    def actividad(self):
        print("Actividad genérica")

class Profesor(Persona):
    def actividad(self):
        print("Enseñando")

kevin_santiago_larrota_cuervo = Profesor()
kevin_santiago_larrota_cuervo.actividad()


#ejemplo 46  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.atributos = {}

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.atributos["altura"] = 1.75
print(kevin_santiago_larrota_cuervo.atributos)
