class Animal:
    def __init__(self,n): self.n=n
    def sonido(self): return ''
class Perro(Animal):
    def sonido(self): return 'Guau'
class Gato(Animal):
    def sonido(self): return 'Miau'

if __name__=='__main__':
    print(Perro('F').sonido(), Gato('G').sonido())
