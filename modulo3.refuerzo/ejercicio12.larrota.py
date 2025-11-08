class Calculadora:
    def sumar(self,a,b): return a+b
    def restar(self,a,b): return a-b
    def dividir(self,a,b):
        if b==0: raise ZeroDivisionError('div/0')
        return a/b

if __name__ == '__main__':
    c = Calculadora(); print(c.sumar(3,4), c.dividir(10,2))
