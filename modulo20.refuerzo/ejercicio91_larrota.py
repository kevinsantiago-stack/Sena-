class Luz:
    def __init__(self):
        self.encendida = False
    def cambiar_estado(self):
        self.encendida = not self.encendida

kevin_santiago_larrota_cuervo = Luz()
kevin_santiago_larrota_cuervo.cambiar_estado()
print(kevin_santiago_larrota_cuervo.encendida)