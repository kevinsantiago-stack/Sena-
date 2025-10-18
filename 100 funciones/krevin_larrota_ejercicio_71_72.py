#ejemplo 71  funciones

def multiplicar_todos_kevin_santiago_larrota_cuervo(lista):
    resultado = 1
    for x in lista:
        resultado *= x
    return resultado

multiplicado_kevin_santiago_larrota_cuervo = multiplicar_todos_kevin_santiago_larrota_cuervo([1,2,3,4])
print(multiplicado_kevin_santiago_larrota_cuervo)


#ejemplo 72  funciones

def lista_negativos_kevin_santiago_larrota_cuervo(lista):
    return [-abs(x) for x in lista]

negativos_kevin_santiago_larrota_cuervo = lista_negativos_kevin_santiago_larrota_cuervo([1,2,3])
print(negativos_kevin_santiago_larrota_cuervo)
