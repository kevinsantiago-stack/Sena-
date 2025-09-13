#17. Pedir números al usuario y calcular su promedio hasta que se ingrese un número negativo

total = 0
contador = 0
while True:
    num = float(input("Ingresa un número (negativo para salir): "))
    if num < 0:
        break
    total += num
    contador += 1
if contador > 0:
    print("Promedio:", total / contador)
else:
    print("No se ingresaron números válidos")