

def invertir_palabras_lista(kevin_santiago_larrota_cuervo_lista):
    return [p[::-1] for p in kevin_santiago_larrota_cuervo_lista]

print(invertir_palabras_lista(["Kevin","Santiago","Cuervo"]))


def ordenar_por_longitud(kevin_santiago_larrota_cuervo_lista):
    return sorted(kevin_santiago_larrota_cuervo_lista, key=len)

print(ordenar_por_longitud(["Kevin","Santiago","Cuervo"]))