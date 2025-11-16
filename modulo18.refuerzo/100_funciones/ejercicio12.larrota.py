
def palabras_con_inicial(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_letra):
    return [p for p in kevin_santiago_larrota_cuervo_lista if p.startswith(kevin_santiago_larrota_cuervo_letra)]

print(palabras_con_inicial(["Kevin","Santiago","Carlos"], "K"))



def reemplazar_palabra(kevin_santiago_larrota_cuervo_texto, kevin_santiago_larrota_cuervo_antigua, kevin_santiago_larrota_cuervo_nueva):
    return kevin_santiago_larrota_cuervo_texto.replace(kevin_santiago_larrota_cuervo_antigua, kevin_santiago_larrota_cuervo_nueva)

print(reemplazar_palabra("Hola Kevin", "Kevin", "Santiago"))