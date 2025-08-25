# crear.py
NOMBRE = input ("escriba su nombre:")
APELLIDO =  input ("escriba su apellido:") 

archivo = open ("archivo.txt","a")
archivo.write (NOMBRE + " " + APELLIDO + "\n")
archivo.close()
print ("datos guardados")


#editar.py
try:
    archivo = open("archivo.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
except:
    print("no existe el archivo")
    exit()

if len(lineas) == 0:
    print("el archivo está vacío")
    exit()

for numero, linea in enumerate(lineas, 1):
    datos = linea.strip().split(",")
    if len(datos) >= 2:
        print(f"{numero}. {datos[0]}, {datos[1]}")
    else:
        print(f"{numero}. {linea.strip()}")

numero_registro = input("Escriba el número de registro a editar: ")
try:
    numero_registro = int(numero_registro)
except ValueError:
    print("Debe ingresar un número válido.")
    exit()

if numero_registro < 1 or numero_registro > len(lineas):
    print("El número de registro no es válido")
    exit()

datos_actuales = lineas[numero_registro - 1].strip().split(",")
print(f"\nEditando registro {numero_registro}")
print(f"Nombre actual: {datos_actuales[0]}")
print(f"Apellido actual: {datos_actuales[0]}")
print("Ingrese los nuevos datos")

nuevo_nombre = input("Ingresar nombre: ")
nuevo_apellido = input("Ingresar apellido: ")
lineas[numero_registro - 1] = f"{nuevo_nombre},{nuevo_apellido}\n"

archivo = open("archivo.txt", "w")
archivo.writelines(lineas)
archivo.close()
print("Registro actualizado")

#eliminar.py

try:
    archivo = open("archivo.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

except:
    print("no existe el archivo")
    exit()
if len(lineas) == 0:
    print("el archivo está vacío")
    exit()

for numero, linea in enumerate (lineas, 1):
    datos = linea.strip().split(" ")
    print(f"{numero}. {datos[0]} {datos[1]}")
    print()

numero_registro = input("Escriba el número de registro a eliminar: ")
numero_registro = int (numero_registro)
if numero_registro < 1 or numero_registro > len(lineas):
    print("El número de registro no es válido")
    exit()

datos_borrar = lineas[numero_registro - 1].strip().split(",")
print (f"\n vas a borrea un registro{numero_registro}")
print (f"nombre a borrar {datos_borrar[0]}")
print (f"apellido a borrar {datos_borrar[1]}")
confirmacion = input("¿Está seguro que desea borrar este registro? (s/n): ")
if confirmacion.lower() == 's':
    del lineas[numero_registro - 1]
    archivo = open("archivo.txt", "w")
    archivo.writelines(lineas)
    archivo.close()
    print("Registro eliminado")
else:
    print("Operación cancelada")

#leer.py
try:
    archivo = open("archivo.txt", "r")

except:
    print ("no existe el archivo")
    exit()
lineas = archivo.readlines()
archivo.close()
 
if len(lineas) == 0:
    print ("el archivo esta vacio")
else:
    print ("el archivo tiene", len(lineas), "lineas")

for numero , lineas in enumerate (lineas):
    lineas_limpiar = lineas.strip()
    datos = lineas_limpiar.split(" ")  

    print (f"registro# {numero}:")
    print (f"nombre : {datos[0] }")
    print (f"apellido : {datos[1] }")
print ("fin del registro")


