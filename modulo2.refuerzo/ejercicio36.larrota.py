class ReservaHotel:
    def __init__(self): self._reservas={}
    def reservar(self,hab,persona): 
        if hab in self._reservas: return False
        self._reservas[hab]=persona; return True
    def cancelar(self,hab): self._reservas.pop(hab,None)

if __name__=='__main__':
    r=ReservaHotel(); print(r.reservar('101','Ana'))
