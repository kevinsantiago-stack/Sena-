class Strategy:
    def ejecutar(self, a,b): return a+b
class Resta(Strategy):
    def ejecutar(self,a,b): return a-b

if __name__=='__main__':
    s=Resta(); print(s.ejecutar(5,2))
