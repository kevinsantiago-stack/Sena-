class PropertyExample:
    def __init__(self,val): self._v=val
    @property
    def v(self): return self._v

if __name__=='__main__':
    p=PropertyExample(10); print(p.v)
