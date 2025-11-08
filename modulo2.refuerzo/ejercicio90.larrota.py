# Ejercicio 90: utilidad generada automáticamente
class Ej90:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej90({self.val})"

if __name__=='__main__':
    e=Ej90(1); e.inc(); e.double(); print(e)
