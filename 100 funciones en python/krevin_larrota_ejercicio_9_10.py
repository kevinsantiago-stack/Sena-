#ejemplo 9  funciones en python 

def es_primo(kevin_santiago_larrota_cuervo):
    if kevin_santiago_larrota_cuervo < 2:
        return False
    for i in range(2, kevin_santiago_larrota_cuervo):
        if kevin_santiago_larrota_cuervo % i == 0:
            return False
    return True

print(es_primo(7))

#ejemplon 10  funciones en python 

def cuadrados(kevin_santiago_larrota_cuervo_lista):
    return [x**2 for x in kevin_santiago_larrota_cuervo_lista]

print(cuadrados([1,2,3,4]))
