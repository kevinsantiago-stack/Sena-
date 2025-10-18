# ejemplo 25 bucles

for kevin in range(3):
    for cuervo in range(3):
        print(f"({kevin},{cuervo})", end=" ")
    print()

# ejemplo 16 bucles 

nombre_completo = "Kevin Santiago Larrota Cuervo"
contador_a = 0
for letra in nombre_completo.lower():
    if letra == 'a':
        contador_a += 1
print("Cantidad de letras 'a':", contador_a)
