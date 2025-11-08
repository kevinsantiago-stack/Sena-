# kevin santiago larrota cuervo
def main():
    n = int(input("¿Cuántos números quieres? "))
    lista = [i**2 for i in range(1, n+1)]
    print("Lista de cuadrados:", lista)

if __name__ == '__main__':
    main()
