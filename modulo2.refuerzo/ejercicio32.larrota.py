class AutoCombustible:
    def __init__(self,cap): self.cap=cap; self.nivel=cap
    def consumir(self,km): 
        uso=km*0.1
        if uso<=self.nivel: self.nivel-=uso; return True
        return False
    def repostar(self,l): self.nivel=min(self.cap,self.nivel+l)

if __name__=='__main__':
    a=AutoCombustible(50); a.consumir(100); print(a.nivel)
