# kevin santiago larrota cuervo
def contar_vocales(frase):
    vocales = "aeiouáéíóú"
    return sum(1 for c in frase.lower() if c in vocales)

def main():
    frase = input("Ingresa una frase: ")
    print(f"La frase tiene {contar_vocales(frase)} vocales.")

if __name__ == '__main__':
    main()
