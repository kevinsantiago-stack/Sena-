#ejemplo 51  funciones en python
def promedio_diccionario(kevin_santiago_larrota_cuervo_dicc):
    return sum(kevin_santiago_larrota_cuervo_dicc.values()) / len(kevin_santiago_larrota_cuervo_dicc)

print(promedio_diccionario({"a":10,"b":20,"c":30}))

#ejemplo 52  funciones en python

def contar_palabras_largas(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_n):
    return len([p for p in kevin_santiago_larrota_cuervo_lista if len(p) > kevin_santiago_larrota_cuervo_n])

print(contar_palabras_largas(["hola","adios","programacion"], 4))

