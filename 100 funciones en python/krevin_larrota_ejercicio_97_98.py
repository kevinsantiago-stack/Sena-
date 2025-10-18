#ejemplo 97  funciones en python

def saludar_persona(kevin_santiago_larrota_cuervo_nombre="Kevin"):
    return f"Hola, {kevin_santiago_larrota_cuervo_nombre}!"

print(saludar_persona())
print(saludar_persona("Santiago"))

#ejemplo 98  funciones en python

def contar_consonantes(kevin_santiago_larrota_cuervo_texto):
    return sum(1 for c in kevin_santiago_larrota_cuervo_texto.lower() if c.isalpha() and c not in "aeiou")

print(contar_consonantes("Kevin Santiago"))
