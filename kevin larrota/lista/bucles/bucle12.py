#12. sumar numeros pares de una lista 

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = 0
for num in lista:
    if num % 2 == 0:
        suma_pares += num
print("Suma de pares:", suma_pares)