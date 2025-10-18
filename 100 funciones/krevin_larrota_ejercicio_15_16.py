# ejemplo 15  funciones 
def concatenar_listas_kevin_santiago_larrota_cuervo(lista1, lista2):
    return lista1 + lista2

listas_kevin_santiago_larrota_cuervo = concatenar_listas_kevin_santiago_larrota_cuervo([1,2],[3,4])
print(listas_kevin_santiago_larrota_cuervo)



# ejemplo 16  funciones  

def contar_vocales_kevin_santiago_larrota_cuervo(palabra):
    return sum(1 for letra in palabra if letra.lower() in "aeiou")

vocales_kevin_santiago_larrota_cuervo = contar_vocales_kevin_santiago_larrota_cuervo("Kevin")
print(vocales_kevin_santiago_larrota_cuervo)
