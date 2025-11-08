def generar_stats_aleatorias():
    import random
    return {'vida': random.randint(80,120),'ataque':random.randint(15,25),'defensa':random.randint(10,20),'suerte':random.randint(1,10)}

if __name__ == '__main__':
    print(generar_stats_aleatorias())
