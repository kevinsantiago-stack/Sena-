

def todas_iguales(kevin_santiago_larrota_cuervo_lista):
    return all(x == kevin_santiago_larrota_cuervo_lista[0] for x in kevin_santiago_larrota_cuervo_lista)

print(todas_iguales(["Kevin","Kevin","Kevin"]))


def contar_letra_lista(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_letra):
    return sum(word.count(kevin_santiago_larrota_cuervo_letra) for word in kevin_santiago_larrota_cuervo_lista)

print(contar_letra_lista(["Kevin","Santiago","Cuervo"], "o"))