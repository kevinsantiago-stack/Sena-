class FactoryProduct:
    def make(self,tipo):
        return {'tipo':tipo}

if __name__=='__main__':
    f=FactoryProduct(); print(f.make('toy'))
