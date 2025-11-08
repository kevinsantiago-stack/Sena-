# Ejercicio 57: utilidad generada automáticamente
class Ej57:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej57({self.val})"

if __name__=='__main__':
    e=Ej57(1); e.inc(); e.double(); print(e)
