# 1 ejercicio
print ("hola mundo")

# 2 ejercicio
nombre ("Juan")
edad = (18)
estudiante = True
promedio = 4.5

print("¡Hola,", nombre, "!")
print("Tienes", edad, "años.")
print("¿Eres estudiante?", estudiante)
print("Tu promedio actual es de", promedio)

# 3 ejercicio
mi_lista = [1,2,3,4,5]
print("Lista:", mi_lista)
print("Tipo:", type(mi_lista))

mi_tupla = (10,20,30)
print("Tupla:", mi_tupla)
print("Tipo:", type(mi_tupla))

mi_diccionario= {"nmbre": "juan": "edad": 18, "ciudad": "bogota"}
print("Diccionario:", mi_diccionario)
print("Tipo:", type(mi_diccionario))

mi_set = {1,2,3,3,4}
print("Set:", mi_set)
print("Tipo:", type(mi_set))

# 4 ejercicio

a 10
b = 3
suma = a + b
resta = ab
multiplicación = a * b
División = A/B
módulo = a% b
potencia = a ** b

print("Suma:", suma)
print("Resto:", resto)
print("Multiplicación:", multiplicacion)
print("División:", división)
print("Módulo (residuo):", módulo)
print("Potencia:", potencia)
print("¿a es igual a b?", a == b)

# 5 ejercicio

edad int(input("¿Cuántos años tienes?"))
Si la edad < 0:
     print("Edad inválida... por favor, ingresa un número positivo.")
Elif Edad < 12:
     print("Eres un niño.")
Elif Edad < 18:
     print("Eres un adolescente.")
Elif edad < 60:
     print("Eres un adulto.")
de lo contrario:
     print("Eres un adulto mayor.")

# 6 ejercicio

print("Bucle for:")
para i en rango(1, 6):
    si i == 3:
        continuar
    print(i)
    si i == 4:
        quebrar


print("\nBucle MIENTRAS:")
contador = 0
Mientras que Contador < 5:
    contador += 1
    if contador == 2:
         continuar
    print(contador)
    if contador == 4:
       break 

# 7 ejercicio

def sumar(a, b):
    resultado = a + b
    devolver resultado

Multiplicador = lambda x, y: x * y

núm1 = 5
núm2 = 3

print("Suma usando función normal:", sumar(num1, num2))
print("Multiplicación usando lambda:", multiplicar (num1, num2))

# 8 ejercicio

Intente:
# Solicitar dos números al usuario
    num1 int(input("Ingresa el primer número: "))
    num2 int(input("Ingresa el segundo número: "))

# Intentar dividirlos
    resultado = num1/num2
    print("El resultado de la división es:", resultado)

excepto ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero...")

excepto ValueError:
    print("¡Error! Solo se permiten números enteros...")

Finalmente:
    print("¡Gracias por usar el programa!")

# 9 ejercicio

Importar matemáticas

número 16

raiz_cuadrada matemáticas.sqrt(numero)
potencia matemáticas.pow(2, 3)
angulo_rad matemáticas.radianes (90)
seno matemáticas.pecado(angulo_rad)

print("Raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("2 elevado a la 3 es:", potencia)
print("Seno de 90 grados es:", seno)
# Importar el módulo datetime
Importar fecha y hora

def saludar (nombre):
    return f"¡Hola, {nombre)! Bienvenido al módulo.")

def cuadrado(n):
    retorno n * n

print(saludar("Juan"))
print("El cuadrado de 5 es:", cuadrado(5))

# ejercicio 10 
class Persona:
     def_init_(self, nombre, edad):
        yo.nombre nombre
        yo.edad edad

     def presentarse(self):
     print(f"Hola... Soy {self.nombre) y tengo (self.edad) años.")

class Estudiante (Persona):
     def __init__(self, nombre, edad, curso):
    super()._init_(nombre, edad)
    yo.curso curso

    def mostrar_curso(yo):
    print(f"Estoy matriculado en el curso: (self.curso)")

personal persona ("Carlos", 40)
estudiante1 Estudiante("Juan", 18, "Programación en Python")

personal.presentarse()
estudiante1.presentarse()
estudiantel.mostrar_curso()



