# kevin santiago larrota cuervo
import requests

def obtener_status(url='https://api.github.com'):
    try:
        r = requests.get(url, timeout=5)
        return r.status_code, r.headers.get('content-type', '')
    except Exception as e:
        return None, str(e)

def main():
    status, info = obtener_status()
    print('Status:', status)
    print('Info:', info)

if __name__ == '__main__':
    main()
