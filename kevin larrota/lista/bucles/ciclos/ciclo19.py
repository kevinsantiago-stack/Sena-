# Ejercicio 4: Invertir palabra
palabra = input("Escribe una palabra: ")
invertida = ""

for letra in palabra:
    invertida = letra + invertida  # va agregando al inicio

print("Palabra invertida:", invertida)
