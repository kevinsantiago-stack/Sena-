#ejemplo 83  funciones en python

def reemplazar_vocales(kevin_santiago_larrota_cuervo_texto):
    return ''.join('*' if c.lower() in "aeiou" else c for c in kevin_santiago_larrota_cuervo_texto)

print(reemplazar_vocales("Kevin Santiago Cuervo"))

#ejemplo 84  funciones en python

def contar_palabras_letra(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_letra):
    return len([p for p in kevin_santiago_larrota_cuervo_lista if kevin_santiago_larrota_cuervo_letra in p])

print(contar_palabras_letra(["Kevin","Santiago","Cuervo"], "a"))
