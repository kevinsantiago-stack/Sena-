class Carrito:
    def __init__(self): self.items={}
    def agregar(self,producto,cantidad=1):
        self.items[producto]=self.items.get(producto,0)+cantidad
    def total(self):
        return sum(p.precio*c for p,c in self.items.items())

if __name__=='__main__':
    class P: 
        def __init__(self,n,p): self.nombre=n; self.precio=p
    p=P('Camisa',20); c=Carrito(); c.agregar(p,2); print(c.total())
