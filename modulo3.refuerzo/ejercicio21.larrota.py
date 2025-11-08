# Ejercicio 21: utilidad generada automáticamente
class Ej21:
    def __init__(self, val=0): self.val=val
    def inc(self): self.val += 1
    def double(self): self.val *= 2

if __name__ == '__main__':
    e = Ej21(1); e.inc(); e.double(); print(e.val)
