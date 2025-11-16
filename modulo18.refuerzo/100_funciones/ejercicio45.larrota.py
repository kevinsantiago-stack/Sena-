

def palabras_largas_n(kevin_santiago_larrota_cuervo_lista, kevin_santiago_larrota_cuervo_n):
    return [p for p in kevin_santiago_larrota_cuervo_lista if len(p) > kevin_santiago_larrota_cuervo_n]

print(palabras_largas_n(["Kevin","Santiago","Cuervo"], 5))



def palabras_y_longitud(kevin_santiago_larrota_cuervo_lista):
    return [(p,len(p)) for p in kevin_santiago_larrota_cuervo_lista]

print(palabras_y_longitud(["Kevin","Santiago","Cuervo"]))