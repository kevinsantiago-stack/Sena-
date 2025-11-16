

def concatenar_palabras(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_separador="-"):
    return kevin_santiago_larrota_cuervo_separador.join(kevin_santiago_larrota_cuervo_lista)

print(concatenar_palabras(["Kevin","Santiago","Cuervo"]))
print(concatenar_palabras(["Kevin","Santiago","Cuervo"], " "))



def contar_vocales_lista(kevin_santiago_larrota_cuervo_lista):
    return [sum(1 for c in p.lower() if c in "aeiou") for p in kevin_santiago_larrota_cuervo_lista]

print(contar_vocales_lista(["Kevin","Santiago","Cuervo"]))