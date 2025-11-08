# Ejercicio 2: Instalar Django (script)
import subprocess, sys
def instalar():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'django'])
if __name__=='__main__': instalar()
