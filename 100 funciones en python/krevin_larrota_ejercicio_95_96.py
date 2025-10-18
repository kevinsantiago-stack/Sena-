#ejemplo 95  funciones en python
def pares_lista_anidada(kevin_santiago_larrota_cuervo_listas):
    return [x for sublist in kevin_santiago_larrota_cuervo_listas for x in sublist if x%2==0]

print(pares_lista_anidada([[1,2,3],[4,5,6]]))


#ejemplo 96  funciones en python

def contar_palabra_lista(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_palabra):
    return kevin_santiago_larrota_cuervo_lista.count(kevin_santiago_larrota_cuervo_palabra)

print(contar_palabra_lista(["Kevin","Santiago","Kevin"], "Kevin"))
