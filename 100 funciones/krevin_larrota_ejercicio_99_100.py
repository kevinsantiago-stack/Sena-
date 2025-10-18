#ejemplo 99  funciones

def solo_pares_kevin_santiago_larrota_cuervo(lista):
    return [x for x in lista if x%2==0]

pares_kevin_santiago_larrota_cuervo = solo_pares_kevin_santiago_larrota_cuervo([1,2,3,4,5])
print(pares_kevin_santiago_larrota_cuervo)


#ejemplo 100  funciones

def intercambiar_extremos_kevin_santiago_larrota_cuervo(lista):
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

intercambiada_kevin_santiago_larrota_cuervo = intercambiar_extremos_kevin_santiago_larrota_cuervo([1,2,3,4])
print(intercambiada_kevin_santiago_larrota_cuervo)
