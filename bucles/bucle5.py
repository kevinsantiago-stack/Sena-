#5. adivina el numero 
import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    intentos += 1

    if intento < numero_secreto:
        print("Muy bajo.")
    elif intento > numero_secreto:
        print("Muy alto.")
    else:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        adivinado = True
