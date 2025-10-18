# ejercicio 93 bucles

lista_cuadrados_kevin_santiago_larrota_cuervo = [x**2 for x in range(1, 11)]
for valor in lista_cuadrados_kevin_santiago_larrota_cuervo:
    print("Cuadrado:", valor)

# ejercicio 94 bucles

palabras_kevin_santiago_larrota_cuervo = ["uva", "manzana", "pera", "avena"]
for palabra in palabras_kevin_santiago_larrota_cuervo:
    if palabra[0].lower() in "aeiou":
        print("Empieza con vocal:", palabra)