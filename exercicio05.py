class Conta():
    def __init__(self, saldo):
        self.saldo = saldo

class ContaCorrente(Conta):
    def __init__(self, saldo=100, limite=50):
        super().__init__(saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo e limite insuficientes.")
        self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f} | Limite: R${self.limite:.2f}")

Conta1 = ContaCorrente()
Conta1.sacar(120)
        