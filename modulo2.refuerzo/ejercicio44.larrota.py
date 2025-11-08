class Serializer:
    def to_dict(self): return self.__dict__
    def to_json(self): import json; return json.dumps(self.to_dict())

if __name__=='__main__':
    class A(Serializer): 
        def __init__(self): self.x=1; self.y='a'
    print(A().to_json())
