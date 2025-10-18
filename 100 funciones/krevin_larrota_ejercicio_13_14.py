# ejemplo 13  funciones 

def es_primo_kevin_santiago_larrota_cuervo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primo_kevin_santiago_larrota_cuervo = es_primo_kevin_santiago_larrota_cuervo(7)
print(primo_kevin_santiago_larrota_cuervo)

# ejemplo 14  funciones 

def mayusculas_kevin_santiago_larrota_cuervo(lista):
    return [x.upper() for x in lista]

mayus_kevin_santiago_larrota_cuervo = mayusculas_kevin_santiago_larrota_cuervo(["hola", "mundo"])
print(mayus_kevin_santiago_larrota_cuervo)
