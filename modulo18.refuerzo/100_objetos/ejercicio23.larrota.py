from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        print("Guau")

kevin_santiago_larrota_cuervo = Perro()
kevin_santiago_larrota_cuervo.sonido()


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

class Juego:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

kevin_santiago_larrota_cuervo = Jugador("Kevin Santiago Larrota Cuervo")
juego1 = Juego()
juego1.agregar_jugador(kevin_santiago_larrota_cuervo)
for j in juego1.jugadores:
    print(j.nombre)