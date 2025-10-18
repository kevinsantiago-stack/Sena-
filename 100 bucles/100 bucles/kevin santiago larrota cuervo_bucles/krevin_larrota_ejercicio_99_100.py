# ejercicio 99 bucles 

palabras_kevin_santiago_larrota_cuervo = ["hola", "python", "kevin"]
for palabra in palabras_kevin_santiago_larrota_cuervo:
    print(palabra.upper())

# ejercicio 100 bucles

a_kevin_santiago_larrota_cuervo, b_kevin_santiago_larrota_cuervo = 0, 1
while a_kevin_santiago_larrota_cuervo <= 100:
    print(a_kevin_santiago_larrota_cuervo)
    a_kevin_santiago_larrota_cuervo, b_kevin_santiago_larrota_cuervo = (
        b_kevin_santiago_larrota_cuervo,
        a_kevin_santiago_larrota_cuervo + b_kevin_santiago_larrota_cuervo,
    )
    