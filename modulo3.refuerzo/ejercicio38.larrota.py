# Ejercicio 38: ejercicio automático
class Ej38:
    def __init__(self, v=0): self.v=v
    def add(self, x): self.v += x
    def reset(self): self.v = 0

if __name__ == '__main__':
    e = Ej38(); e.add(5); print(e.v)
