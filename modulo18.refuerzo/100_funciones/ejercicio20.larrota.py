

def filtrar_palabras_letra(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_letra):
    return [p for p in kevin_santiago_larrota_cuervo_lista if kevin_santiago_larrota_cuervo_letra in p]

print(filtrar_palabras_letra(["Kevin","Santiago","Carlos"], "a"))




def invertir_palabras(kevin_santiago_larrota_cuervo_lista):
    return [p[::-1] for p in kevin_santiago_larrota_cuervo_lista]

print(invertir_palabras(["Kevin","Santiago"]))