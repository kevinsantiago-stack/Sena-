def calcular_promedio():
    calificaciones = []
    print("Ingresa 5 calificaciones (0-100):")
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Calificación {i+1}: "))
                if 0 <= nota <= 100:
                    calificaciones.append(nota)
                    break
                print("La nota debe estar entre 0 y 100")
            except ValueError:
                print("Ingresa un número válido")
    promedio = sum(calificaciones) / len(calificaciones)
    if promedio >= 90: letra = "A"
    elif promedio >= 80: letra = "B"
    elif promedio >= 70: letra = "C"
    elif promedio >= 60: letra = "D"
    else: letra = "F"
    print(f"Promedio: {promedio:.1f} - Calificación: {letra}")

if __name__ == '__main__':
    calcular_promedio()
