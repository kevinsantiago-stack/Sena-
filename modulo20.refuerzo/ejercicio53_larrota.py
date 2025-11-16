class Empleado:
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    def info(self):
        print(f"{self.nombre} trabaja como {self.cargo}")

kevin_santiago_larrota_cuervo = Empleado("Kevin Santiago Larrota Cuervo", "Ingeniero")
kevin_santiago_larrota_cuervo.info()
def cuadrados_mayores_que(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_n):
    return [x**2 for x in kevin_santiago_larrota_cuervo_lista if x**2 > kevin_santiago_larrota_cuervo_n]

print(cuadrados_mayores_que([1,2,3,4,5], 10))



def numeros_pares(kevin_santiago_larrota_cuervo_inicio, kevin_santiago_larrota_cuervo_fin):
    return [x for x in range(kevin_santiago_larrota_cuervo_inicio, kevin_santiago_larrota_cuervo_fin+1) if x%2==0]

print(numeros_pares(1,10))