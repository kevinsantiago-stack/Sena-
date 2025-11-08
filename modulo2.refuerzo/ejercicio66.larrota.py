# Ejercicio 66: utilidad generada automáticamente
class Ej66:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej66({self.val})"

if __name__=='__main__':
    e=Ej66(1); e.inc(); e.double(); print(e)
