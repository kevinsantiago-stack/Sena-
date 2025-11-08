# kevin santiago larrota cuervo
class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad < 0 or edad > 150:
        raise EdadInvalidaError(f'Edad {edad} no es válida')
    return edad

def main():
    try:
        validar_edad(-5)
    except EdadInvalidaError as e:
        print('Error de validación:', e)
    else:
        print('Edad válida')

if __name__ == '__main__':
    main()
