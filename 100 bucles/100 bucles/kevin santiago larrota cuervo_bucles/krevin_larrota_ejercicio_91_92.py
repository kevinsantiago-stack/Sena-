# ejercicio 91 bucles

estudiantes_kevin_santiago_larrota_cuervo = {
    "Ana": {"edad": 20, "nota": 4.5},
    "Luis": {"edad": 22, "nota": 4.2}
}
for nombre, datos in estudiantes_kevin_santiago_larrota_cuervo.items():
    print(nombre, "-> edad:", datos["edad"], ", nota:", datos["nota"])

# ejercicio 92 bucles

total_kevin_santiago_larrota_cuervo = 0
num = 1
while total_kevin_santiago_larrota_cuervo < 50:
    total_kevin_santiago_larrota_cuervo += num
    num += 1
print("Total acumulado:", total_kevin_santiago_larrota_cuervo)