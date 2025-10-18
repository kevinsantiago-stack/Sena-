#ejemplo 67  funciones en python

def crear_sumador(kevin_santiago_larrota_cuervo_n):
    def sumador(kevin_santiago_larrota_cuervo_x):
        return kevin_santiago_larrota_cuervo_n + kevin_santiago_larrota_cuervo_x
    return sumador

sumar_5 = crear_sumador(5)
print(sumar_5(10))


#ejemplo 68  funciones en python

def palabras_vocal_inicial(kevin_santiago_larrota_cuervo_lista):
    return [p for p in kevin_santiago_larrota_cuervo_lista if p[0].lower() in "aeiou"]

print(palabras_vocal_inicial(["Kevin","Ana","Oscar","Santiago"]))
