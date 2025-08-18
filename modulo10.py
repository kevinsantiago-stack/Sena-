  #Clases y Objetos
#Una clase es como un molde (define cómo será algo).
#Un objeto es una instancia creada a partir de la clase.
# Definición de clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Ana", 20)
persona2 = Persona("Luis", 25)

print(persona1.nombre, persona1.edad)
print(persona2.nombre, persona2.edad)

#Atributos y Métodos
#Atributos → características (variables dentro de la clase).
#Métodos → funciones dentro de la clase.
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def encender(self):
        print(f"El coche {self.marca} {self.modelo} está encendido")

mi_coche = Coche("Toyota", "Corolla")
mi_coche.encender()


#Encapsulación
#Permite proteger datos internos.
#Convenciones en Python:
#Público → variable
#Protegido → _variable
#Privado → __variable

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular       # Público
        self._tipo = "Ahorros"       # Protegido
        self.__saldo = saldo         # Privado
    
    def ver_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Carlos", 5000)
print(cuenta.titular)
print(cuenta._tipo)          
print(cuenta.ver_saldo())


#Herencia
#Una clase puede heredar atributos y métodos de otra.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        print("Este animal hace un sonido")

class Perro(Animal):
    def sonido(self):
        print("Guau guau")

perro = Perro("Firulais")
perro.sonido()


#Polimorfismo
#Permite que métodos con el mismo nombre tengan comportamientos diferentes según la clase.

class Gato:
    def sonido(self):
        return "Miau"

class Perro:
    def sonido(self):
        return "Guau"

animales = [Gato(), Perro()]

for animal in animales:
    print(anima.sonido())
