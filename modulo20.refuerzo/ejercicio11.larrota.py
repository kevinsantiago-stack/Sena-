 

class Banco:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    def mostrar_saldo(self):
        print(self.__saldo)

kevin_santiago_larrota_cuervo = Banco("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.mostrar_saldo()




