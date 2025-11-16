

def frecuencia(kevin_santiago_larrota_cuervo_lista):
    freq = {}
    for x in kevin_santiago_larrota_cuervo_lista:
        freq[x] = freq.get(x, 0) + 1
    return freq

print(frecuencia([1,2,2,3,3,3]))



def lista_pares(kevin_santiago_larrota_cuervo_n):
    return [x for x in range(1, kevin_santiago_larrota_cuervo_n+1) if x % 2 == 0]

print(lista_pares(10))