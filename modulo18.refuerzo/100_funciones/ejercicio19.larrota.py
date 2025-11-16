

def multiplicar_lista(kevin_santiago_larrota_cuervo_lista):
    resultado = 1
    for x in kevin_santiago_larrota_cuervo_lista:
        resultado *= x
    return resultado

print(multiplicar_lista([1,2,3,4]))




def contar_mayores(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_valor):
    return len([x for x in kevin_santiago_larrota_cuervo_lista if x > kevin_santiago_larrota_cuervo_valor])

print(contar_mayores([1,5,10,2], 4))