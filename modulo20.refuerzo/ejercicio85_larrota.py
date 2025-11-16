class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.datos = {}

kevin_santiago_larrota_cuervo = Persona("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.datos["edad"] = 25
print(kevin_santiago_larrota_cuervo.datos)