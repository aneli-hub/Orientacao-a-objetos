
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return True

    def sacar(self, valor):
        if self.saldo <= valor:
            self.saldo = self.valor - valor
            return True
        else:
            return False
    
    def get_saldo(self):
        return self.saldo
    
contaAneli = ContaBancaria(1000)

contaAneli.sacar(50)
contaAneli.depositar(70)

print(contaAneli.get_saldo())   