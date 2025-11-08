# kevin santiago larrota cuervo
import os, shutil, time
from pathlib import Path

def limpiar_temporales(carpeta='temp', max_age_seconds=7*24*3600):
    p = Path(carpeta)
    p.mkdir(exist_ok=True)
    now = time.time()
    removed = 0
    for f in p.iterdir():
        if f.is_file() and now - f.stat().st_mtime > max_age_seconds:
            f.unlink()
            removed += 1
    return removed

def main():
    Path('temp').mkdir(exist_ok=True)
    print('Archivos eliminados:', limpiar_temporales('temp', max_age_seconds=0))  # forzar limpieza

if __name__ == '__main__':
    main()
