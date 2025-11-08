class SingletonCounter:
    _inst=None
    def __new__(cls): 
        if not cls._inst: cls._inst=super().__new__(cls); cls._inst.n=0
        return cls._inst
    def inc(self): self.n+=1

if __name__=='__main__':
    a=SingletonCounter(); b=SingletonCounter(); a.inc(); print(b.n)
