def elegir_arma(armas):
    for i,a in enumerate(armas,1): print(i,a)
    while True:
        try:
            ix = int(input('Elige arma: '))
            if 1<=ix<=len(armas): return armas[ix-1]
        except ValueError:
            pass
        print('Entrada inválida')

if __name__ == '__main__':
    print(elegir_arma(['Hacha','Espada','Aro']))
