def es_email_valido(email):
    e = email.strip().lower()
    return '@' in e and '.' in e and not e.startswith('@')

if __name__ == '__main__':
    print(es_email_valido('juan@gmail.com'))
