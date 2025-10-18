# ejemplo 19 funciones 

class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.set_nombre("Kevin Cuervo")
print(kevin_santiago_larrota_cuervo.get_nombre())

# ejemplo 20 funciones 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.set_edad(edad)
    def set_edad(self, edad):
        if edad >= 0:
            self.edad = edad
        else:
            self.edad = 0
    def mostrar(self):
        print(f"{self.nombre} tiene {self.edad} años")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo", 25)
kevin_santiago_larrota_cuervo.mostrar()
