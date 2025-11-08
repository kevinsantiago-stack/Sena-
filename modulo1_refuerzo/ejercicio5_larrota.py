# kevin santiago larrota cuervo
def main():
    frutas = ['manzana', 'banana', 'naranja']
    frutas.append('uva')
    frutas.insert(1, 'pera')
    frutas.remove('pera')
    fruta_eliminada = frutas.pop()
    print('Frutas:', frutas)
    print('Fruta eliminada:', fruta_eliminada)

    numeros = [10, 25, 3, 47, 12]
    numeros.sort()
    print('Números ordenados:', numeros)

if __name__ == '__main__':
    main()
