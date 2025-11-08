from dataclasses import dataclass
@dataclass
class Item:
    id:int
    nombre:str

if __name__=='__main__':
    it=Item(1,'x'); print(it)
