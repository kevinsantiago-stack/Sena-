# Ejemplo de encontrar el segundo número más grande en una tupla
numeros = (70, 20, 10, 50, 30)

ordenados = sorted(numeros, reverse=True)
segundo_mayor = ordenados[1]

print("El segundo número más grande es:", segundo_mayor)