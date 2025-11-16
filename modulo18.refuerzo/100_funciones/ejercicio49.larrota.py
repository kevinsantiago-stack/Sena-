

def mayusculas_filtradas(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_letra):
    return [p.upper() for p in kevin_santiago_larrota_cuervo_lista if p.startswith(kevin_santiago_larrota_cuervo_letra)]

print(mayusculas_filtradas(["Kevin","Santiago","Cuervo"], "K"))


def contar_digitos(kevin_santiago_larrota_cuervo_texto):
    return sum(1 for c in kevin_santiago_larrota_cuervo_texto if c.isdigit())

print(contar_digitos("Kevin123Santiago456"))