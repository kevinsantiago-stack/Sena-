# Ejercicio 79: utilidad generada automáticamente
class Ej79:
    def __init__(self,val=0): self.val=val
    def inc(self): self.val+=1
    def double(self): self.val*=2
    def __repr__(self): return f"Ej79({self.val})"

if __name__=='__main__':
    e=Ej79(1); e.inc(); e.double(); print(e)
