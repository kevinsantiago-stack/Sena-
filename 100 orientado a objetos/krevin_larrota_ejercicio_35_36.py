#ejemplo 35 funciones 

class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

kevin_santiago_larrota_cuervo = Atleta()
kevin_santiago_larrota_cuervo.nadar()
kevin_santiago_larrota_cuervo.correr()

 # ejemplo 36 funciones 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.datos["edad"] = 25
print(kevin_santiago_larrota_cuervo.datos)
