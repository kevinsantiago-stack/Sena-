#ejemplo 65  funciones en python

def promedio_dicc(kevin_santiago_larrota_cuervo_dicc):
    if not kevin_santiago_larrota_cuervo_dicc:
        return 0
    return sum(kevin_santiago_larrota_cuervo_dicc.values()) / len(kevin_santiago_larrota_cuervo_dicc)

print(promedio_dicc({"a":10,"b":20}))

#ejemplo 66  funciones en python

def claves_mayores(kevin_santiago_larrota_cuervo_dicc, kevin_santiago_larrota_cuervo_valor):
    return [k for k,v in kevin_santiago_larrota_cuervo_dicc.items() if v > kevin_santiago_larrota_cuervo_valor]

print(claves_mayores({"a":5,"b":10,"c":15}, 7))
