# 1 ejercicio

def evaluar_persona(edad, ingreso, ciudad):
    Si la edad < 18:
      return "Menor de edad"
    ELIF edad >= 18 e ingreso < 1000:
      return "Adulto con ingresos bajos"
    ELIF edad >= 18 e ingreso >= 1000 y ciudad.lower() == "Bogotá":
      return "Adulto con ingresos altos en Bogotá"
    de lo contrario:
      return "Adulto con ingresos altos fuera de Bogotá"

#Ejemplo de uso
print(evaluar_persona (16, 500, "Medellín"))
print(evaluar_persona (25, 800, "Cali"))
print(evaluar_persona (30, 1500, "Bogotá"))
grabado(evaluar_persona (40, 2000, "Barranquilla"))

#2 ejercicio 

def calcular_descuento (cantidad):
    if cantidad == 0:
      return "No hay compra, no hay descuento"
    elif cantidad < 5:
      return "Descuento del 5%"
    elif cantidad < 10:
      return "Descuento del 10%"
    de lo contrario:
      return "Descuento del 20%"

print(calcular_descuento(0))
print(calcular_descuento(3))
print(calcular_descuento(7))
print(calcular_descuento(15))
      
# 3 ejercicio

def  calcular_descuento_especial (cantidad, es_cliente_vip):
       si cantidad == 0 o no es_cliente_vip:
           return "No hay descuento especial"
       elif cantidad >= 5 y cantidad < 10 y es_cliente_vip:
           return "Descuento especial del 15%"
       elif cantidad >= 10 y es_cliente_vip:
           return "Descuento especial del 25%"
       de lo contrario: 
           return "Descuento especial del 5%"

print(calcular_descuento_especial(0, True))
print(calcular_descuento_especial(7, Falso))
print(calcular_descuento_especial(7, True)) 
print(calcular_descuento_especial(12, True)) 
print(calcular_descuento_especial(3, True))
      
      
