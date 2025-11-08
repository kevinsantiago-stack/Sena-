class RegistroPartidas:
    def __init__(self): self._partidas = []
    def registrar(self, nombre): import datetime; self._partidas.append({'nombre':nombre,'ts':datetime.datetime.now().isoformat()})
    def listar(self): return list(self._partidas)

if __name__ == '__main__':
    r = RegistroPartidas(); r.registrar('Ana'); print(r.listar())
