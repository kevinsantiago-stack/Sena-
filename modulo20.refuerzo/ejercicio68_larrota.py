class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def interes(self, porcentaje):
        self.saldo += self.saldo * porcentaje / 100

kevin_santiago_larrota_cuervo = Cuenta("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.interes(5)
print(kevin_santiago_larrota_cuervo.saldo)