# ejercicio 85 bucles 

suma_cuadrados = 0
for kevin_santiago_larrota_cuervo in range(1, 6):
    suma_cuadrados += kevin_santiago_larrota_cuervo ** 2
print("Suma de cuadrados:", suma_cuadrados)

# ejercicio 86 bucles 

nombres = ["Kevin", "Santiago", "Larrota"]
edades = [20, 21, 22]
for nombre, edad in zip(nombres, edades):
    print(nombre, "tiene", edad, "años")