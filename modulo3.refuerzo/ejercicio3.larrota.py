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

def calculadora_rpg():
    clases = {
        "Guerrero": {"vida_mult": 10, "ataque_mult": 3, "defensa_mult": 4},
        "Mago": {"vida_mult": 5, "ataque_mult": 6, "defensa_mult": 2},
        "Arquero": {"vida_mult": 7, "ataque_mult": 5, "defensa_mult": 3},
        "Clérigo": {"vida_mult": 8, "ataque_mult": 2, "defensa_mult": 5}
    }
    while True:
        try:
            nivel = int(input("Nivel del personaje (1-50): "))
            if 1 <= nivel <= 50:
                break
            print("Nivel fuera de rango")
        except ValueError:
            print("Ingresa un número válido")
    nombres = list(clases.keys())
    idx = mostrar_menu(nombres, "SELECCIONA LA CLASE")
    elegido = nombres[idx]
    mult = clases[elegido]
    vida = 50 + (nivel * mult["vida_mult"])
    ataque = 10 + (nivel * mult["ataque_mult"])
    defensa = 5 + (nivel * mult["defensa_mult"])
    print(f"=== {elegido.upper()} NIVEL {nivel} ===")
    print(f"Vida: {vida} - Ataque: {ataque} - Defensa: {defensa}")

if __name__ == '__main__':
    calculadora_rpg()
