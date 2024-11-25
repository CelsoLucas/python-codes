class BombaDeCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoC = tipoCombustivel
        self.valorL = valorLitro
        self.qtdC = quantidadeCombustivel

    def abastecerPorValor(self):
        self.valor = float(input("Digite o valor a ser abastecido: R$"))

    def abastecerPorLitro(self):
        pass
    def alterarValor(self):
        pass
    def alterarCombustivel(self):
        pass
    def alterarQuatidadeCombustivel(self):
        pass