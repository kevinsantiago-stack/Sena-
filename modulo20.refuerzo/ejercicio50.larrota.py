
class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1
    @classmethod
    def total_personas(cls):
        return cls.contador

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
otra_persona = Persona("Juan")
print(Persona.total_personas())


