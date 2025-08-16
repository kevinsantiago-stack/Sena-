while True:
    numero = int(input("Ingresa un número (mayor a 100 para salir): "))

    if numero < 0:
        print("Número negativo, inténtalo de nuevo.")
        continue  # Salta a la siguiente iteración

    if numero > 100:
        print("¡Correcto! El número es mayor a 100.")
        break  # Sale del bucle

    print("Ese número no es mayor a 100, sigue intentando.")

#ejercicio 2 

filas = 7
for i in range(1, filas + 1):
    print("*" * i)
