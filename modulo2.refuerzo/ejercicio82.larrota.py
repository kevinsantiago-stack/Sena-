# Ejercicio 82: utilidad generada automáticamente
class Ej82:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej82({self.val})"

if __name__=='__main__':
    e=Ej82(1); e.inc(); e.double(); print(e)
