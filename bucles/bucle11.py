#11.  determinar si un numero es primo 

num = 10
es_primo = True
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        es_primo = False
        break
print("Es primo" if es_primo else "No es primo")