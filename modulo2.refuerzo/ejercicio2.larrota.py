class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = float(saldo)
    def depositar(self, monto):
        if monto>0:
            self._saldo += monto
    def retirar(self, monto):
        if 0<monto<=self._saldo:
            self._saldo -= monto
            return True
        return False
    def saldo(self):
        return self._saldo

if __name__ == "__main__":
    c = CuentaBancaria("Juan", 100)
    c.depositar(50)
    print(c.saldo())
