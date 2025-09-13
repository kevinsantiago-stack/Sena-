#7. sumar solo los numeros impres de una lista

lista = [1, 2, 3, 4, 5, 6, 7]
suma = 0
for num in lista:
    if num % 2 != 0:
        suma += num
print(suma)
print(input("--------------"))
