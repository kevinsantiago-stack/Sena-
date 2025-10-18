#ejemplo 57  funciones

def longitud_strings_kevin_santiago_larrota_cuervo(lista):
    return [len(x) for x in lista]

longitudes_kevin_santiago_larrota_cuervo = longitud_strings_kevin_santiago_larrota_cuervo(["Kevin", "Hola"])
print(longitudes_kevin_santiago_larrota_cuervo)


#ejemplo 58  funciones

def pares_hasta_n_kevin_santiago_larrota_cuervo(n):
    return [x for x in range(n+1) if x % 2 == 0]

pares_hasta_kevin_santiago_larrota_cuervo = pares_hasta_n_kevin_santiago_larrota_cuervo(10)
print(pares_hasta_kevin_santiago_larrota_cuervo)
