# Ejercicio 91: utilidad final
class Ej91:
    def __init__(self, v=0): self.v=v
    def op(self): self.v = (self.v+1)*2
if __name__ == '__main__':
    e = Ej91(2); e.op(); print(e.v)
