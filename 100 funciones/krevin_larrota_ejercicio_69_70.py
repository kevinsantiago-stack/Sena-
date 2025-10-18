#ejemplo 69  funciones

def invertir_palabras_kevin_santiago_larrota_cuervo(lista):
    return [palabra[::-1] for palabra in lista]

invertidas_kevin_santiago_larrota_cuervo = invertir_palabras_kevin_santiago_larrota_cuervo(["Hola","Kevin"])
print(invertidas_kevin_santiago_larrota_cuervo)


#ejemplo 70  funciones

def contar_positivos_kevin_santiago_larrota_cuervo(lista):
    return len([x for x in lista if x > 0])

positivos_kevin_santiago_larrota_cuervo = contar_positivos_kevin_santiago_larrota_cuervo([-1,2,3,-4])
print(positivos_kevin_santiago_larrota_cuervo)
