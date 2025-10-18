#ejemplo 69  funciones

class Animal:
    def hablar(self):
        print("Algún sonido")

class Gato(Animal):
    def hablar(self):
        print("Miau")

kevin_santiago_larrota_cuervo = Gato()
kevin_santiago_larrota_cuervo.hablar()


#ejemplo 70  funciones

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
