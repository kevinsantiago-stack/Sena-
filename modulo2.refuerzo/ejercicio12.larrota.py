class Estudiante:
    def __init__(self,nombre):
        self.nombre=nombre; self.materias={}
    def inscribir(self,materia,creditos): self.materias[materia]={'creditos':creditos,'nota':None}
    def poner_nota(self,materia,nota): self.materias[materia]['nota']=nota
    def promedio(self):
        notas=[m['nota'] for m in self.materias.values() if m['nota'] is not None]
        return sum(notas)/len(notas) if notas else 0

if __name__=='__main__':
    s=Estudiante('Luis'); s.inscribir('Mat',4); s.poner_nota('Mat',4.5); print(s.promedio())
