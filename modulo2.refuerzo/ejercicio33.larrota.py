class Parking:
    def __init__(self,plazas): self.plazas=plazas; self.ocupados=0
    def entrar(self):
        if self.ocupados<self.plazas: self.ocupados+=1; return True
        return False
    def salir(self): 
        if self.ocupados>0: self.ocupados-=1; return True
        return False

if __name__=='__main__':
    p=Parking(2); print(p.entrar(), p.entrar(), p.entrar(), p.salir(), p.entrar())
