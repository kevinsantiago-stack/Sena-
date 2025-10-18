# ejemplo 13  funciones 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f"Persona: {self.nombre}"

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(kevin_santiago_larrota_cuervo)

# ejemplo 14  funciones 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"Persona('{self.nombre}')"

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(repr(kevin_santiago_larrota_cuervo))
