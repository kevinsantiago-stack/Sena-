#kevin santiago larrota cuervo

# ejemplo 5  funciones 

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

kevin_santiago_larrota_cuervo = Estudiante("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.estudiar()

#ejemplo 6  funciones 

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
    def mostrar_nombre(self):
        print(self.__nombre)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.mostrar_nombre()
