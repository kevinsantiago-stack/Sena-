class Notificador:
    def __init__(self): self._logs=[]
    def enviar(self,msg): self._logs.append(msg)
    def logs(self): return list(self._logs)

if __name__=='__main__':
    n=Notificador(); n.enviar('Hola'); print(n.logs())
