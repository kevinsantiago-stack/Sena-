class Zoo:
    def __init__(self): self.animales=[]
    def agregar(self,a): self.animales.append(a)
    def sonidos(self): return [a.sonido() for a in self.animales]

if __name__=='__main__':
    class A: 
        def __init__(self,n): self.n=n
        def sonido(self): return 'x'
    z=Zoo(); z.agregar(A('x')); print(z.sonidos())
