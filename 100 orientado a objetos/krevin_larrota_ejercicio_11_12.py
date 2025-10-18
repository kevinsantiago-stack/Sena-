# ejemplo 11  funciones 

class Deportista:
    def entrenar(self):
        print("Entrenando")

class Musico:
    def tocar(self):
        print("Tocando instrumento")

class Persona(Deportista, Musico):
    def __init__(self, nombre):
        self.nombre = nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.entrenar()
kevin_santiago_larrota_cuervo.tocar()

#ejemplo 12 funciones

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hobbies = []
    def agregar_hobby(self, hobby):
        self.hobbies.append(hobby)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.agregar_hobby("Fútbol")
print(kevin_santiago_larrota_cuervo.hobbies)
