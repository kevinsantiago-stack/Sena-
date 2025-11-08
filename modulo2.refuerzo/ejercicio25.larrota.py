class HashMap:
    def __init__(self): self._d={}
    def set(self,k,v): self._d[k]=v
    def get(self,k,default=None): return self._d.get(k,default)

if __name__=='__main__':
    h=HashMap(); h.set('a',1); print(h.get('a'))
