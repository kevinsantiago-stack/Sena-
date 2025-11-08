# kevin santiago larrota cuervo
import math

def main():
    n = int(input("Ingresa un número entero: "))
    if n < 0:
        print("No existe el factorial de un número negativo.")
    else:
        print(f"El factorial de {n} es {math.factorial(n)}")

if __name__ == '__main__':
    main()
