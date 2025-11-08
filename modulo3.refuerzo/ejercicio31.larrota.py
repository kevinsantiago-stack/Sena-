def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            v = int(input(mensaje))
            if minimo is not None and v < minimo: print('Valor muy bajo'); continue
            if maximo is not None and v > maximo: print('Valor muy alto'); continue
            return v
        except ValueError:
            print('Ingresa un número válido')

if __name__ == '__main__':
    print(pedir_entero('Ingresa un entero (1-100): ', 1, 100))
