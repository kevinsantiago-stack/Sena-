class SingletonConfig:
    _inst=None
    def __new__(cls,**k):
        if not cls._inst: cls._inst=super().__new__(cls); cls._inst.cfg={}
        return cls._inst
    def set(self,k,v): self.cfg[k]=v
    def get(self,k,default=None): return self.cfg.get(k,default)

if __name__=='__main__':
    a=SingletonConfig(); b=SingletonConfig(); a.set('x',1); print(b.get('x'))
