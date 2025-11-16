 

class Secreto:
    def __init__(self, mensaje):
        self.__mensaje = mensaje
    def revelar(self):
        print(self.__mensaje)

kevin_santiago_larrota_cuervo = Secreto("Kevin Santiago Larrota Cuervo")
kevin_santiago_larrota_cuervo.revelar()

