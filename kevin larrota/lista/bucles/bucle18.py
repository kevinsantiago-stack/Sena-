#18. calcular la suma de digitos de un numero

num = int(input("Ingresa un número: "))
suma = 0
while num > 0:
    suma += num % 10
    num //= 10
print("Suma de dígitos:", suma)