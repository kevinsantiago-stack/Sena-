# ejercicio 89 

numero_kevin_santiago_larrota_cuervo = 12
for divisor in range(1, numero_kevin_santiago_larrota_cuervo + 1):
    if numero_kevin_santiago_larrota_cuervo % divisor == 0:
        print("Divisor:", divisor) 

# ejercicio 90

frase_kevin_santiago_larrota_cuervo = "Hola Kevin Santiago"
contador = 0
for c in frase_kevin_santiago_larrota_cuervo:
    if c != " ":
        contador += 1
print("Caracteres sin espacios:", contador)