
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje/100)

kevin_santiago_larrota_cuervo = Producto("Camisa", 50)
kevin_santiago_larrota_cuervo.aplicar_descuento(20)
print(kevin_santiago_larrota_cuervo.precio)




