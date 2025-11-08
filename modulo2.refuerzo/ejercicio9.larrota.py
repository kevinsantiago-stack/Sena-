class Pedido:
    def __init__(self, id_, items=None):
        self.id = id_; self.items = items or []; self.estado='CREADO'
    def pagar(self): self.estado='PAGADO'
    def enviar(self): 
        if self.estado=='PAGADO': self.estado='ENVIADO'; return True
        return False

if __name__ == '__main__':
    p=Pedido(1,['item1','item2']); p.pagar(); print(p.enviar(), p.estado)
