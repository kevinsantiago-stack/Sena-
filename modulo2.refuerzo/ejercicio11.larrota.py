class Empleado:
    def __init__(self,nombre,id_,puesto,salario):
        self.nombre=nombre; self.id=id_; self.puesto=puesto; self.salario=salario
    def aumentar(self,pc): self.salario*=1+pc/100

if __name__=='__main__':
    e=Empleado('Rosa',1,'Dev',1000); e.aumentar(10); print(e.salario)
