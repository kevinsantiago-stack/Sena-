#ejemplo 9  funciones 

def factorial_kevin_santiago_larrota_cuervo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_kevin_santiago_larrota_cuervo(n-1)

fact_kevin_santiago_larrota_cuervo = factorial_kevin_santiago_larrota_cuervo(5)
print(fact_kevin_santiago_larrota_cuervo)


#ejemplon 10  funciones 

def invertir_cadena_kevin_santiago_larrota_cuervo(cadena):
    return cadena[::-1]

invertido_kevin_santiago_larrota_cuervo = invertir_cadena_kevin_santiago_larrota_cuervo("Kevin")
print(invertido_kevin_santiago_larrota_cuervo)

