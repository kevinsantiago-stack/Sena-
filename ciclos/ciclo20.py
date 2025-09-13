# Ejercicio 5: Primos entre 1 y 50
num = 2
while num <= 50:
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
    num += 1
