class ObserverList:
    def __init__(self): self._obs=[]
    def add(self,o): self._obs.append(o)
    def notify(self,v): [o(v) for o in self._obs]

if __name__=='__main__':
    ol=ObserverList(); ol.add(lambda x: print('o',x)); ol.notify(5)
