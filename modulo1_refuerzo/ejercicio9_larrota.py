# kevin santiago larrota cuervo
import json
from pathlib import Path

def main():
    Path('data').mkdir(exist_ok=True)
    usuarios = [{'nombre':'Ana','edad':30}, {'nombre':'Luis','edad':25}]
    Path('data/users.json').write_text(json.dumps(usuarios, ensure_ascii=False, indent=2))
    print('Archivo data/users.json creado.')
    # Lectura
    contenido = Path('data/users.json').read_text(encoding='utf-8')
    print('Contenido JSON:\n', contenido)

if __name__ == '__main__':
    main()
