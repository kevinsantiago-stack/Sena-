#15. pedir numeros al usuario hasta que ingrese un 0

while True:
    num = int(input("Ingresa un número (0 para salir): "))
    if num == 0:
        break
    print("Número ingresado:", num)