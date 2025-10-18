#ejemplo 61  funciones en python

def sumar_listas(kevin_santiago_larrota_cuervo_listas):
    return [sum(lst) for lst in kevin_santiago_larrota_cuervo_listas]

print(sumar_listas([[1,2,3],[4,5,6],[7,8]]))


#ejemplo 62  funciones en python

def matriz_identidad(kevin_santiago_larrota_cuervo_n):
    return [[1 if i==j else 0 for j in range(kevin_santiago_larrota_cuervo_n)] for i in range(kevin_santiago_larrota_cuervo_n)]

print(matriz_identidad(3))
