class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.saver = self.idade
        self.idade = int(input("Idade: "))

    def engordar(self):
        pass

    def emagrecer(self):
        pass

    def crescer(self):
        if self.idade < 21:
            for i in range(self.idade - self.saver):
                self.altura = self.altura + 0.05

pessoa1 = Pessoa("Celso", 17, 65, 1.70)
print(f"{pessoa1.nome} tem {pessoa1.idade} e tem {pessoa1.altura} de altura")
pessoa1.envelhecer()
pessoa1.crescer()
print(f"Agora {pessoa1.nome} tem {pessoa1.idade} e tem {pessoa1.altura} de altura")