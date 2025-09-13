# Ejercicio 3: Tablas de multiplicar del 1 al 5
for i in range(1, 6):  # Tablas del 1 al 5
    print(f"\nTabla del {i}")
    for j in range(1, 11):  # Multiplicar del 1 al 10
        print(f"{i} x {j} = {i*j}")
