import random
def adivina_numero():
    secreto = random.randint(1, 10)
    while True:
        try:
            intento = int(input('Adivina un número (1-10): '))
            if intento == secreto:
                print('¡Correcto!')
                break
            elif intento < secreto:
                print('Muy bajo')
            else:
                print('Muy alto')
        except ValueError:
            print('Ingresa un número válido')

if __name__ == '__main__':
    adivina_numero()
