# kevin santiago larrota cuervo
def main():
    print("=== PROGRAMA INTERACTIVO ===")
    nombre = input("holaa como te llamas?? ")
    apellido = input("dime cual es tu apellido ")
    edad = int(input("¿Cuántos años tienes? "))
    altura = float(input("¿Cuál es tu altura en metros? (ej: 1.75) "))
    peso = float(input("¿Cuál es tu peso en kg? "))
    imc = peso / (altura ** 2)
    año_actual = 2025
    año_nacimiento = año_actual - edad

    print("\n" + "="*30)
    print(f"Nombre completo: {nombre} {apellido}")
    print(f"Edad: {edad} años")
    print(f"Año de nacimiento aproximado: {año_nacimiento}")
    print(f"Altura: {altura} m, Peso: {peso} kg")
    print(f"IMC: {imc:.2f}")

if __name__ == '__main__':
    main()
