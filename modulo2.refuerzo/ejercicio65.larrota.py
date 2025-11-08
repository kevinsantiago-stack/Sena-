# Ejercicio 65: utilidad generada automáticamente
class Ej65:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej65({self.val})"

if __name__=='__main__':
    e=Ej65(1); e.inc(); e.double(); print(e)
