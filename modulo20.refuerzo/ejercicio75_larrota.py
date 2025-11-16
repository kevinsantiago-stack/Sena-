class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

kevin_santiago_larrota_cuervo = CuentaBancaria("Kevin Santiago Larrota Cuervo", 1000)
kevin_santiago_larrota_cuervo.retirar(200)
print(kevin_santiago_larrota_cuervo.saldo)