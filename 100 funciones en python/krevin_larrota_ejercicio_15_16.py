# ejemplo 15  funciones en python 
def contar_vocales(kevin_santiago_larrota_cuervo):
    return sum(1 for c in kevin_santiago_larrota_cuervo.lower() if c in "aeiou")

print(contar_vocales("Kevin Santiago"))


# ejemplo 16  funciones  en python 

def promedio(kevin_santiago_larrota_cuervo_lista):
    return sum(kevin_santiago_larrota_cuervo_lista) / len(kevin_santiago_larrota_cuervo_lista)

print(promedio([10, 20, 30]))
