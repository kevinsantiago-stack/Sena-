# kevin santiago larrota cuervo
def main():
    n = int(input("Ingresa un número para su tabla de multiplicar: "))
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    main()
