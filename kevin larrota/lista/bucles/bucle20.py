#20 contar cuantos numeros pares e impares hay en una lista

lista = [12, 7, 9, 14, 20, 33, 41, 56]
pares = 0
impares = 0

for num in lista:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Numeros impares:¨{impares}")