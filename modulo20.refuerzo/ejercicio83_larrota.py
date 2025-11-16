class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def __len__(self):
        return len(self.nombre)

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
print(len(kevin_santiago_larrota_cuervo))