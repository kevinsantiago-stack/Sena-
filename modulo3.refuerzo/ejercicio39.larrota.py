# Ejercicio 39: ejercicio automático
class Ej39:
    def __init__(self, v=0): self.v=v
    def add(self, x): self.v += x
    def reset(self): self.v = 0

if __name__ == '__main__':
    e = Ej39(); e.add(5); print(e.v)
