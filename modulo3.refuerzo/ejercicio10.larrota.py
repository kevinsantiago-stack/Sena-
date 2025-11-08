def guardar_texto(path, texto):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(texto)
def leer_texto(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == '__main__':
    p = '/mnt/data/temp_guardado.txt'
    guardar_texto(p, 'hola mundo')
    print(leer_texto(p))
