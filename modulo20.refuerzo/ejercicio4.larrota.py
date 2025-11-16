

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

kevin_santiago_larrota_cuervo1 = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo2 = Persona("Kevin Santiago Larrota Cuervo")
print(Persona.contador)


