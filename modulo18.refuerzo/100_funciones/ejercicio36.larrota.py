

def cuadrados_pares(kevin_santiago_larrota_cuervo_lista):
    return [x**2 for x in kevin_santiago_larrota_cuervo_lista if x % 2 == 0]

print(cuadrados_pares([1,2,3,4,5]))



def tuplas_a_dicc(kevin_santiago_larrota_cuervo_lista):
    return {k:v for k,v in kevin_santiago_larrota_cuervo_lista}

print(tuplas_a_dicc([("a",1),("b",2)]))