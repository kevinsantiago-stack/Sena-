class PersonaProp:
    def __init__(self,n): self._n=n
    @property
    def nombre(self): return self._n
    @nombre.setter
    def nombre(self,v): 
        if not v: raise ValueError('inv'); self._n=v

if __name__=='__main__':
    p=PersonaProp('Ana'); print(p.nombre); p.nombre='Lu'; print(p.nombre)
