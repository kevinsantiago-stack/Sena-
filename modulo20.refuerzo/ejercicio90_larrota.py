class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def crear_hijo(self):
        return Persona(self.nombre + " Jr.")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
hijo = kevin_santiago_larrota_cuervo.crear_hijo()
print(hijo.nombre)