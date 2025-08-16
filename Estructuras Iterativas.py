cuadrado = lambda x: x ** 2
print(f"El cuadrado de 4 es: {cuadrado(4)}")

Multiplicador = lambda a, b: a * b
print(f"5 x 3 = {Multiplicador(5, 3)}")

def aplicar_operacion(operacion, num1, num2):
    return operacion(num1, num2)

resultado = aplicar_operacion(lambda x, y: x - y, 10, 4)
print(f"Resultado de la resta: {resultado}")

#ejemplo 2 

mensaje_global = "Hola como estás?"

def saludar(nombre, edad=18):
    mensaje_local = f"Hola {nombre}, tienes {edad} años."
    print(mensaje_local)

def sumar(a, b):
    resultado = a + b
    return resultado

saludar("Kevin", 25)
saludar(nombre="Laura")

total = sumar(10, 20)
print(f"La suma es: {total}")

print(mensaje_global)
