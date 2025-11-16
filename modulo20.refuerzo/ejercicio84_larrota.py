class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        print("Miau")

kevin_santiago_larrota_cuervo = Gato()
kevin_santiago_larrota_cuervo.sonido()