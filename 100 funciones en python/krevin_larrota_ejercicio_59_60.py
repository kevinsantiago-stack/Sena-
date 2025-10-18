#ejemplo 59  funciones en python
def divisores(kevin_santiago_larrota_cuervo_num):
    return [x for x in range(1, kevin_santiago_larrota_cuervo_num+1) if kevin_santiago_larrota_cuervo_num % x == 0]

print(divisores(12))


#ejemplo 60  funciones en python

def palabras_unicas(kevin_santiago_larrota_cuervo_lista):
    return len(set(kevin_santiago_larrota_cuervo_lista))

print(palabras_unicas(["hola","mundo","hola"]))
