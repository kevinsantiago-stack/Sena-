class ChatSimple:
    def __init__(self): self.hist=[]
    def enviar(self,u,msg): self.hist.append((u,msg))
    def ultimo(self): return self.hist[-1] if self.hist else None

if __name__=='__main__':
    c=ChatSimple(); c.enviar('u1','hola'); print(c.ultimo())
