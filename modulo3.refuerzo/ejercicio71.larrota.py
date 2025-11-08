import json
def guardar_ranking(ranking, archivo='/mnt/data/ranking.txt'):
    with open(archivo, 'a', encoding='utf-8') as f:
        for nombre, puntos in ranking:
            f.write(f'{nombre},{puntos}\n')
def mostrar_ranking(archivo='/mnt/data/ranking.txt'):
    try:
        jugadores = []
        with open(archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                n,p = linea.strip().split(',')
                jugadores.append((n,int(p)))
        jugadores.sort(key=lambda x: x[1], reverse=True)
        return jugadores[:10]
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    guardar_ranking([('Ana',100),('Lu',80)])
    print(mostrar_ranking())
