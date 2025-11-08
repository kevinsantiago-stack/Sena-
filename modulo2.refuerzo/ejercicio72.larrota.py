# Ejercicio 72: utilidad generada automáticamente
class Ej72:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej72({self.val})"

if __name__=='__main__':
    e=Ej72(1); e.inc(); e.double(); print(e)
