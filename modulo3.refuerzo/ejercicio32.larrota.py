def limpiar_lista_y_ordenar(lista):
    return sorted([x.strip().title() for x in lista if isinstance(x, str)])

if __name__ == '__main__':
    print(limpiar_lista_y_ordenar(['  vikingo','samurai',' caballero  ']))
