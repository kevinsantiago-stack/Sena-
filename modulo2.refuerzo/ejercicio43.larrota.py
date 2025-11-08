class SimpleFile:
    def __init__(self,path): self.path=path
    def write(self,text): open(self.path,'w').write(text)
    def read(self): return open(self.path).read()

if __name__=='__main__':
    f=SimpleFile('/mnt/data/tmp.txt'); f.write('hola'); print(f.read())
