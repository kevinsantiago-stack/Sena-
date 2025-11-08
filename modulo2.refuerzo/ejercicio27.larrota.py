class CacheSimple:
    def __init__(self): self._d={}
    def set(self,k,v): self._d[k]=v
    def get(self,k,default=None): return self._d.get(k,default)

if __name__=='__main__':
    c=CacheSimple(); c.set('x',10); print(c.get('x'))
