#ejemplo 63  funciones en python

def es_anagrama(kevin_santiago_larrota_cuervo_1, kevin_santiago_larrota_cuervo_2):
    return sorted(kevin_santiago_larrota_cuervo_1.lower()) == sorted(kevin_santiago_larrota_cuervo_2.lower())

print(es_anagrama("Roma", "Amor"))


#ejemplo 64  funciones en python
def contar_mayores_listas(kevin_santiago_larrota_cuervo_listas, kevin_santiago_larrota_cuervo_valor):
    return [len([x for x in lst if x > kevin_santiago_larrota_cuervo_valor]) for lst in kevin_santiago_larrota_cuervo_listas]

print(contar_mayores_listas([[1,2,3],[4,5,6]], 3))
