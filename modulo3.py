# 1 ejercicio listas
compras ["pan", "leche", "huevos", "arroz"]

print("Lista original:", compras)

compras.append("café") 
print("Después de agregar café:", compras)

compras.insert(2, "frutas") #en python de cuenta desde 0
print("Después de insertar frutas en la posición 2:", compras)

compras.remove("leche") 
print("Después de eliminar leche:", compras)

compras.ordenar()
print("Lista ordenada alfabéticamente:", compras)

producto "arroz"
Si producto en compras:
    print(f"¡{producto) sí está en la lista!")
de lo contrario:

    print (f"(producto) no está en la lista...")

print("Total de productos en la lista:", len(compras))


# 2 ejercicio tuplas

colores = ("rojo", "verde", "azul")

print("Colores disponibles:", colores)

print("Primer color:", colores[0])
print("Segundo color:", colores[1])
print("Tercer color:", colores [2])
#en 'Python se cuenta desde 0,1,2 ect.'
print("Total de colores:", len(colores))

# 3 ejercicio diccionarios

persona = {
    "nombre": "kevin",
    "edad": 17,
    "ciudad": "Bogotá"
}

print("Nombre:", persona ["nombre"])
print("Edad:", persona ["edad"])
print("Ciudad:", persona ["ciudad"])

persona ["profesión"] = "Ingeniero"
print("Después de agregar profesión:", persona)

persona ["edad"] = 17
print("Edad actualizada:", persona)

del persona ["ciudad"]
print("Después de eliminar la ciudad:", persona)


# 4 ejercicio range

para i en rango(5): print("Número:", i)

Impresión("------")

para i en rango(1, 6): print("Contando desde 1:", i)

Impresión("------")

para i en rango (0, 11, 2):

print("De dos en dos:", i)

# 5 ejercicio conjuntos (sets)

animales {"perro", "gato", "loro", "gato", "pez"}

print("Animales en el conjunto:", animales)

animales.add("conejo")
print("Después de agregar conejo:", animales)

animales.add("gato")
print("Después de intentar agregar 'gato' otra vez:", animales)

animales.remove("pez")
print("Después de eliminar pez:", animales)

Si "perro" en Animales:
    print("¡El perro sí está en el conjunto!")
de lo contrario:
    print("El perro no está en el conjunto...")

print("Cantidad total de animales:", len(animales))




