class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def duplicar(self):
        return Persona(self.nombre + " Jr.")

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
nuevo_kevin = kevin_santiago_larrota_cuervo.duplicar()
print(nuevo_kevin.nombre)