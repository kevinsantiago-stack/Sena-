class Vuelo:
    def __init__(self,codigo,capacidad): self.codigo=codigo; self.capacidad=capacidad; self.pasajeros=[]
    def embarcar(self,nombre):
        if len(self.pasajeros)<self.capacidad: self.pasajeros.append(nombre); return True
        return False

if __name__=='__main__':
    v=Vuelo('AV100',2); print(v.embarcar('A'), v.embarcar('B'), v.embarcar('C'))
