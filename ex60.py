class BichinhoVirtual():
    def __init__(self):
        self.nome = "Sem nome"
        self.fome = 0
        self.saude = 10
        self.idade = 0
        self.humor = 10

    def alt_nome(self):
        self.nome = str(input("Digite o novo nome: "))
        print(f"O novo nome é {self.nome}")

    def alt_fome(self):
        self.fome = int(input("Fome 0/10: "))
        print(f"A fome está em {self.fome}")
        self.humor = (self.saude + self.fome) / 2

    def alt_saude(self):
        self.saude = int(input("Saude 0/10: "))
        print(f"A saúde está em {self.saude}")
        self.humor = (self.saude + self.fome) / 2

    def alt_idade(self):
        self.idade = int(input("Nova idade: "))
        print(f"Agora {self.nome} tem {self.idade} anos")

    def alt_humor(self):
        self.humor = (self.saude + self.fome) / 2
        if self.humor == 10:
            print(f"{self.nome} está muito Feliz!")
        elif self.humor >= 8:
            print(f"{self.nome} está Feliz!")
        elif self.humor >= 6:
            print(f"{self.nome} está neutro")
        elif self.humor >= 4:
            print(f"{self.nome} está Bravo!")
        elif self.humor >= 0:
            print(f"{self.nome} está muito Bravo!")

bicho = BichinhoVirtual()
bicho.alt_nome()
bicho.alt_fome()
bicho.alt_saude()
bicho.alt_idade()
bicho.alt_humor()