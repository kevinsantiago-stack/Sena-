#ejemplo 89  funciones

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.inventario = []
    def agregar_producto(self, producto):
        self.inventario.append(producto)

kevin_santiago_larrota_cuervo = Producto("Laptop", 5)
mi_tienda = Tienda()
mi_tienda.agregar_producto(kevin_santiago_larrota_cuervo)
print([(p.nombre, p.cantidad) for p in mi_tienda.inventario])


#ejemplo 90  funciones

class Vehiculo:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
    def frenar(self, decremento):
        self.velocidad -= decremento

kevin_santiago_larrota_cuervo = Vehiculo("Coche", 60)
kevin_santiago_larrota_cuervo.acelerar(20)
kevin_santiago_larrota_cuervo.frenar(10)
print(kevin_santiago_larrota_cuervo.velocidad)
