# Ejercicio 1: Crear entorno virtual (script)
import venv, os
def crear_venv(path='venv'):
    venv.EnvBuilder(with_pip=True).create(path)
if __name__=='__main__': crear_venv()
