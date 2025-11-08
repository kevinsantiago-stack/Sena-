def limpiar_nombre(nombre_sucio):
    return nombre_sucio.strip().title()

def es_email_valido(email):
    email = email.strip().lower()
    return '@' in email and '.' in email and not email.startswith('@')

if __name__ == '__main__':
    print(limpiar_nombre('  maría garcía  '))
    print(es_email_valido('juan@gmail.com'), es_email_valido('@err.com'))
