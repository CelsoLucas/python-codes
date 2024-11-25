class ContaCorrente():
    def __init__(self, num_conta, nome_correntista, saldo):
        self.num_conta = num_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self):
        self.nome_correntista = str(input("Novo nome: "))

    def deposito(self):
        self.dep = float(input("Quanto você deseja depositar: R$"))
        self.saldo = self.saldo + self.dep

    def saque(self):
        self.saque = float(input("Quanto você deseja sacar: R$"))
        self.saldo = self.saldo - self.saque

conta1 = ContaCorrente(12345, "Celso", 1000)
conta1.alterar_nome()
conta1.deposito()
conta1.saque()
print(conta1.nome_correntista)
print(f"R${conta1.saldo}")