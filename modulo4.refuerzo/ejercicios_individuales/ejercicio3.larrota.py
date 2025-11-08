# Ejercicio 3: Crear proyecto (simulado)
import subprocess, sys, os
def startproject(name='mi_sitio'):
    subprocess.check_call([sys.executable, '-m', 'django', 'startproject', name])
if __name__=='__main__': print('Ejercicio: ejecutar startproject en terminal') 
