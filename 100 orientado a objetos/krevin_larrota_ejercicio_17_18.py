# ejemplo 17  funciones 

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

kevin_santiago_larrota_cuervo1 = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo2 = Persona("Kevin Santiago Larrota Cuervo")
print(Persona.contador)


# ejemplo 18  funciones 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

personas = []
personas.append(Persona("Kevin Santiago Larrota Cuervo"))
personas.append(Persona("Juan"))
for p in personas:
    print(p.nombre)
