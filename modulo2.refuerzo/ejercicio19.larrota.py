class Contador:
    def __init__(self,n=0): self.n=n
    def __iter__(self): return self
    def __next__(self):
        if self.n>0:
            val=self.n; self.n-=1; return val
        raise StopIteration

if __name__=='__main__':
    for x in Contador(3): print(x)
