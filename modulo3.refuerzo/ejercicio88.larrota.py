# Ejercicio 88: utilidad final
class Ej88:
    def __init__(self, v=0): self.v=v
    def op(self): self.v = (self.v+1)*2
if __name__ == '__main__':
    e = Ej88(2); e.op(); print(e.v)
