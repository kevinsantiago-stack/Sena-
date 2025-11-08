class CalculadoraHist:
    def __init__(self): self.hist=[]
    def operar(self,a,b,op):
        ops={'+':a+b,'-':a-b,'*':a*b,'/':a/b if b!=0 else None}
        res=ops.get(op); self.hist.append((a,b,op,res)); return res

if __name__=='__main__':
    ch=CalculadoraHist(); print(ch.operar(4,2,'/'), ch.hist)
