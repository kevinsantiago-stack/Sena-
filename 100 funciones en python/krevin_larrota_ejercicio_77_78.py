#ejemplo 77  funciones en python

def filtrar_clave(kevin_santiago_larrota_cuervo_dicc, kevin_santiago_larrota_cuervo_clave):
    return {k:v for k,v in kevin_santiago_larrota_cuervo_dicc.items() if kevin_santiago_larrota_cuervo_clave in k}

print(filtrar_clave({"Kevin":1,"Santiago":2,"Cuervo":3}, "K"))


#ejemplo 78  funciones en python
def divisibles_por(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_n):
    return [x for x in kevin_santiago_larrota_cuervo_lista if x % kevin_santiago_larrota_cuervo_n == 0]

print(divisibles_por([1,2,3,4,5,6], 2))
