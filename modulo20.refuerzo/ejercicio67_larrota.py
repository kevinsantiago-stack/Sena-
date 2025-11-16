class Contraseña:
    def __init__(self, clave):
        self.__clave = clave
    def mostrar_clave(self):
        print(self.__clave)

kevin_santiago_larrota_cuervo = Contraseña("12345")
kevin_santiago_larrota_cuervo.mostrar_clave()