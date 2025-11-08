class Observer:
    def __init__(self): self._callbacks=[]
    def suscribir(self,fn): self._callbacks.append(fn)
    def notificar(self,msg): 
        for f in self._callbacks: f(msg)

if __name__=='__main__':
    obs=Observer()
    obs.suscribir(lambda m: print('Recibido:',m))
    obs.notificar('hola')
