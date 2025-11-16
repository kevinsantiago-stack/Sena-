

def promedio_lista(kevin_santiago_larrota_cuervo_lista):
    if not kevin_santiago_larrota_cuervo_lista:
        return "Lista vacía"
    return sum(kevin_santiago_larrota_cuervo_lista) / len(kevin_santiago_larrota_cuervo_lista)

print(promedio_lista([10,20,30]))
print(promedio_lista([]))




def buscar_elemento(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_elemento):
    return kevin_santiago_larrota_cuervo_elemento in kevin_santiago_larrota_cuervo_lista

print(buscar_elemento([1,2,3], 2))