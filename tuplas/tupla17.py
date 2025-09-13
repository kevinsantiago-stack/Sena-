# Ejemplo de modificación de un elemento en una tupla
tupla = (20, 40, 60)
lista = list(tupla)
lista[1] = 200
tupla_modificada = tuple(lista)
print(tupla_modificada)