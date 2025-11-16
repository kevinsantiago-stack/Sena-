class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad

kevin_santiago_larrota_cuervo = Cuenta("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.depositar(500)
print(kevin_santiago_larrota_cuervo.saldo)