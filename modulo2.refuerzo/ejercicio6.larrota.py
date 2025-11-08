class Calculadora:
    def sumar(self,a,b): return a+b
    def restar(self,a,b): return a-b
    def multiplicar(self,a,b): return a*b
    def dividir(self,a,b):
        if b==0: raise ZeroDivisionError("division por cero")
        return a/b

if __name__ == "__main__":
    calc = Calculadora()
    print(calc.sumar(3,4), calc.dividir(10,2))
