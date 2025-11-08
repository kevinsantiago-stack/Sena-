def contar_palabras(texto):
    palabras = texto.split()
    return {'total_palabras': len(palabras), 'total_caracteres': len(texto), 'palabra_mas_larga': max(palabras, key=len) if palabras else ''}

if __name__ == '__main__':
    print(contar_palabras('Python es un lenguaje de programación extraordinario'))
