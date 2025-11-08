# kevin santiago larrota cuervo

import requests
from bs4 import BeautifulSoup

def obtener_titulo(url='https://example.com'):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.title.string if soup.title else 'Sin título'
        return title
    except Exception as e:
        return f'Error: {e}'

def main():
    print('Título de example.com ->', obtener_titulo('https://example.com'))

if __name__ == '__main__':
    main()
