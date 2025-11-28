# kevin santiago larrota cuervo
def clasificar_edad(edad):
    if edad < 0:
        return "Edad inválida"
    if edad <= 12:
        return "Niño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"

def main():
    edad = int(input("ingresa tu edad: "))
    print(clasificar_edad(edad))

if __name__ == '__main__':
    main()
