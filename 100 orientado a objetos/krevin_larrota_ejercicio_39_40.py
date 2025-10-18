#ejemplo 39 funciones

class Persona:
    contador = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.contador += 1

kevin_santiago_larrota_cuervo1 = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo2 = Persona("Kevin Cuervo")
print(Persona.contador)


#ejemplo 40  funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(len(kevin_santiago_larrota_cuervo))
