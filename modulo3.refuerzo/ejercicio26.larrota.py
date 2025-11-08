# Ejercicio 26: utilidad generada automáticamente
class Ej26:
    def __init__(self, val=0): self.val=val
    def inc(self): self.val += 1
    def double(self): self.val *= 2

if __name__ == '__main__':
    e = Ej26(1); e.inc(); e.double(); print(e.val)
