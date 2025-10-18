#ejemplo 55  funciones en python

def filtrar_diccionario(kevin_santiago_larrota_cuervo_dicc, kevin_santiago_larrota_cuervo_valor):
    return {k:v for k,v in kevin_santiago_larrota_cuervo_dicc.items() if v > kevin_santiago_larrota_cuervo_valor}

print(filtrar_diccionario({"a":10,"b":20,"c":5}, 8))

#ejemplo 56  funciones en python

def reemplazar_lista(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_ant, kevin_santiago_larrota_cuervo_nuev):
    return [x.replace(kevin_santiago_larrota_cuervo_ant, kevin_santiago_larrota_cuervo_nuev) for x in kevin_santiago_larrota_cuervo_lista]

print(reemplazar_lista(["hola","hola mundo"], "hola","adios"))
