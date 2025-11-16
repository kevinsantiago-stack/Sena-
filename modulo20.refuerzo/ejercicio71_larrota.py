class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    def __init__(self, nombre):
        self.nombre = nombre

kevin_santiago_larrota_cuervo = Atleta("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.nadar()
kevin_santiago_larrota_cuervo.correr()