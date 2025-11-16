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

