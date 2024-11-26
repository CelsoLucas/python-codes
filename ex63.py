class BombaDeCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoC = tipoCombustivel
        self.valorL = valorLitro
        self.qtdC = quantidadeCombustivel

    def abastecerPorValor(self):
        self.valor = float(input("Digite o valor a ser abastecido: R$"))
        self.qtd_tot_litros = self.valor / self.valorL
        print(f"A quantidade de litros que ira ser colocada no veiculo é {self.qtd_tot_litros:.2f}")
        self.qtdC -= self.qtd_tot_litros

    def abastecerPorLitro(self):
        self.litro = float(input("Quantidade de litros que você quer: "))
        self.tot_valor = self.litro * self.valorL
        print(f"Para abastecer {self.litro} vai ser R${self.tot_valor}")

    def alterarValor(self):
        self.valorL = float(input("Novo valor do litro: R$"))

    def alterarCombustivel(self):
        self.tipoC = str(input("Novo tipo de combustivel: "))
        
    def alterarQuatidadeCombustivel(self):
        self.qtdC = float(input("Nova quantidade de combustivel: "))

bomba1 = BombaDeCombustivel("Gás", 6, 100)
bomba1.abastecerPorValor()
bomba1.abastecerPorLitro()
