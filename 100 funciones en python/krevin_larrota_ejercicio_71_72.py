#ejemplo 71  funciones en python

def caracteres_unicos(kevin_santiago_larrota_cuervo_texto):
    return len(set(kevin_santiago_larrota_cuervo_texto))

print(caracteres_unicos("Kevin Santiago"))


#ejemplo 72  funciones en python

def primeros_primos(kevin_santiago_larrota_cuervo_n):
    primos = []
    num = 2
    while len(primos) < kevin_santiago_larrota_cuervo_n:
        if all(num % x != 0 for x in range(2,num)):
            primos.append(num)
        num += 1
    return primos

print(primeros_primos(5))
