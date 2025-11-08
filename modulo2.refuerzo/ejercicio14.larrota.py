class Singleton:
    _inst=None
    def __new__(cls,*a,**k):
        if cls._inst is None: cls._inst=super().__new__(cls)
        return cls._inst
    def __init__(self,val=None): 
        if not hasattr(self,'v'): self.v=val

if __name__=='__main__':
    a=Singleton(1); b=Singleton(2); print(a is b, a.v)
