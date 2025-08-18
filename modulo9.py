#Que es un modulo en python?

#Los modulos son archivos 
#que contienen codigo python 
#(funcionees, variables, clases)
#y permiten organizar el codigo en partes
#mas pequeñas y reutilizables.


import matH
print(math.sqrt(16))  

import random
print(random.randint(1, 10))

#Además de los módulos estándar,
#existen librerías creadas por la comunidad 
#que se pueden instalar con pip.
#NumPy → cálculos numéricos.
#pandas → análisis de datos.
#matplotlib → gráficos.

import numpy as np
import pandas as pd

# NumPy
arr = np.array([1, 2, 3, 4])
print(arr * 2)  

# pandas
data = {"Nombre": ["Ana", "Luis", "Carlos"], "Edad": [23, 30, 28]}
df = pd.DataFrame(data)
print(df)

#también puedO crear mis propios modulos
#y reutilizarlos en otros proyectos.
#Para crear un modulo, simplemente creo un archivo .py

def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b
#en mi programa principal lo utilizaria de la siguiente manera 

import mimodulo

print(mimodulo.saludar("Kevin"))
print(mimodulo.sumar(5, 3))

#import importa todo el módulo.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
#from ... import ... importa solo lo que necesitas

import math
print(math.factorial(5))  

from math import factorial
print(factorial(5))       


