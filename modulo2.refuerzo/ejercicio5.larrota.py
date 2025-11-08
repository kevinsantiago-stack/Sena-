from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self): pass

class Circulo(Figura):
    def __init__(self, r): self.r = r
    def area(self): return math.pi*self.r*self.r

class Rectangulo(Figura):
    def __init__(self,a,b): self.a=a; self.b=b
    def area(self): return self.a*self.b

if __name__ == "__main__":
    print(round(Circulo(2).area(),2), Rectangulo(2,3).area())
