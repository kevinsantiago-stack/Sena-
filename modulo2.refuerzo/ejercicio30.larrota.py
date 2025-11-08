class Orden:
    def __init__(self,id_): self.id=id_; self.estado='CREADA'
    def pagar(self): self.estado='PAGADA'
    def enviar(self): 
        if self.estado=='PAGADA': self.estado='ENVIADA'; return True
        return False

if __name__=='__main__':
    o=Orden(1); o.pagar(); print(o.enviar(), o.estado)
