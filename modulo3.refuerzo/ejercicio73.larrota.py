def formatear_tabla(datos):
    # datos: lista de tuplas (nombre, puntos)
    ancho = max(len(str(x[0])) for x in datos)+2
    lines = ['RANKING'.center(ancho+8)]
    for i,(n,p) in enumerate(datos,1):
        lines.append(f'{i:2d}. {n:<{ancho}} {p:>6d}')
    return '\n'.join(lines)
if __name__ == '__main__':
    print(formatear_tabla([('Ana',100),('Lu',80)]))
