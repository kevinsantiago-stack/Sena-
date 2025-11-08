class Contacto:
    def __init__(self,nombre,telefono):
        self.nombre=nombre; self.telefono=telefono

class Agenda:
    def __init__(self): self._contactos=[]
    def agregar(self,c): self._contactos.append(c)
    def buscar(self,n): return [c for c in self._contactos if n.lower() in c.nombre.lower()]

if __name__ == "__main__":
    ag=Agenda(); ag.agregar(Contacto('Luis','300')); print(ag.buscar('lu')[0].telefono)
