class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self):
        self.cor = str(input("Digite a Nova cor: "))

    def mostra_cor(self):
        print(f"A nova cor é {self.cor}")

bola1 = Bola("Preta", 20, "PVC")
print(f"Cor: {bola1.cor}")
bola1.troca_cor()
bola1.mostra_cor()