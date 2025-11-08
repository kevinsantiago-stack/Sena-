import json
class JSONStore:
    def __init__(self, path): self.path=path
    def guardar(self, obj): open(self.path,'w').write(json.dumps(obj))
    def cargar(self): return json.loads(open(self.path).read())

if __name__ == "__main__":
    js=JSONStore('/mnt/data/tmp_store.json'); js.guardar({'x':1}); print(js.cargar())
