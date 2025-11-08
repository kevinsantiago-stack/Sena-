import json
def guardar_perfil_jugador(jugador, archivo='perfil.json'):
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(jugador, f, indent=4, ensure_ascii=False)
def cargar_perfil_jugador(archivo='perfil.json'):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

if __name__ == '__main__':
    mi_jugador = {
        'nombre': 'DragonSlayer', 'nivel':25, 'oro':2500
    }
    guardar_perfil_jugador(mi_jugador)
    print(cargar_perfil_jugador())
