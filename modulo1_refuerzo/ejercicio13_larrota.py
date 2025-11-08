# kevin santiago larrota cuervo
import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None

def main():
    emails = ['test@example.com', 'malo@ejemplo', 'otro.ok@mail.co']
    for e in emails:
        print(e, '->', validar_email(e))

if __name__ == '__main__':
    main()
