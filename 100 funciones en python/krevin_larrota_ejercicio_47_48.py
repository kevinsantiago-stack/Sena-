#ejemplo 47  funciones en python

def diccionario_indice(kevin_santiago_larrota_cuervo_lista):
    return {i: kevin_santiago_larrota_cuervo_lista[i] for i in range(len(kevin_santiago_larrota_cuervo_lista))}

print(diccionario_indice(["a","b","c"]))


#ejemplo 48  funciones en python

def sumar_pares_impares(kevin_santiago_larrota_cuervo_lista):
    pares = sum(x for x in kevin_santiago_larrota_cuervo_lista if x % 2 == 0)
    impares = sum(x for x in kevin_santiago_larrota_cuervo_lista if x % 2 != 0)
    return pares, impares

print(sumar_pares_impares([1,2,3,4,5]))
