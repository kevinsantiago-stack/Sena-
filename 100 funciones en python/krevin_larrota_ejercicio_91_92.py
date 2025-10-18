#ejemplo 91  funciones en python

def suma_dicc_valores(kevin_santiago_larrota_cuervo_lista_dicc, kevin_santiago_larrota_cuervo_clave):
    return sum(d[kevin_santiago_larrota_cuervo_clave] for d in kevin_santiago_larrota_cuervo_lista_dicc)

print(suma_dicc_valores([{"a":10},{"a":20},{"a":5}], "a"))


#ejemplo 92  funciones en python

def filtrar_valores_impares(kevin_santiago_larrota_cuervo_dicc):
    return {k:v for k,v in kevin_santiago_larrota_cuervo_dicc.items() if v%2!=0}

print(filtrar_valores_impares({"a":1,"b":2,"c":3}))
