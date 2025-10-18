#ejemplo 77  funciones

def contar_mayusculas_kevin_santiago_larrota_cuervo(texto):
    return sum(1 for x in texto if x.isupper())

mayusculas_kevin_santiago_larrota_cuervo = contar_mayusculas_kevin_santiago_larrota_cuervo("KevinSantiago")
print(mayusculas_kevin_santiago_larrota_cuervo)


#ejemplo 78  funciones

def contar_minusculas_kevin_santiago_larrota_cuervo(texto):
    return sum(1 for x in texto if x.islower())

minusculas_kevin_santiago_larrota_cuervo = contar_minusculas_kevin_santiago_larrota_cuervo("KevinSantiago")
print(minusculas_kevin_santiago_larrota_cuervo)
