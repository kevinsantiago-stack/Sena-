#ejemplo 99  funciones en python

def palabras_unicas_lista(kevin_santiago_larrota_cuervo_lista):
    return list(set(kevin_santiago_larrota_cuervo_lista))

print(palabras_unicas_lista(["Kevin","Santiago","Kevin"]))


#ejemplo 100  funciones en python

def palabras_longitud_par(kevin_santiago_larrota_cuervo_lista):
    return len([p for p in kevin_santiago_larrota_cuervo_lista if len(p)%2==0])

print(palabras_longitud_par(["Kevin","Santiago","Cuervo"]))
