class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Atleta(Nadador, Corredor):
    pass

kevin_santiago_larrota_cuervo = Atleta()
kevin_santiago_larrota_cuervo.nadar()
kevin_santiago_larrota_cuervo.correr()