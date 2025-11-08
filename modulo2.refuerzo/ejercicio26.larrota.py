class CSVMock:
    def __init__(self,path): self.path=path
    def escribir(self,rows):
        open(self.path,'w').write('\n'.join([','.join(map(str,r)) for r in rows]))
    def leer(self):
        return [line.split(',') for line in open(self.path).read().splitlines()]

if __name__=='__main__':
    cm=CSVMock('/mnt/data/tmpcsv.csv'); cm.escribir([[1,2],[3,4]]); print(cm.leer())
