def mostrar_menu(opciones, titulo):
    print("\n" + "="*40)
    print(titulo.center(40))
    print("="*40)
    for i, opt in enumerate(opciones, 1):
        print(f"{i}. {opt}")
    while True:
        try:
            ele = int(input("Elige una opción: "))
            if 1 <= ele <= len(opciones):
                return ele-1
            print("Opción fuera de rango.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")

if __name__ == '__main__':
    comidas = ["Pizza", "Hamburguesa", "Tacos", "Sushi", "Pasta"]
    idx = mostrar_menu(comidas, "ELIGE TU COMIDA FAVORITA")
    print(comidas[idx])
