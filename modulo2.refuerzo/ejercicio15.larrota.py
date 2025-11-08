class Factory:
    def crear(self,tipo):
        if tipo=='A': return {'tipo':'A'}
        if tipo=='B': return {'tipo':'B'}
        return None

if __name__=='__main__':
    f=Factory(); print(f.crear('A'))
