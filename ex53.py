class Netflix():
    def __init__(self, nome, email, cpf, plano, cartao_de_credito, fone, lista_filmes):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.plano = plano
        self.cartao_de_credito = cartao_de_credito
        self.fone = fone
        self.lista_filmes = lista_filmes

    def assistirFilme(self):
        cont = 0
        for f in self.lista_filmes:
            print(f"{cont} - {f}")
            cont += 1
        opc = int(input("Digite o filme que deseja: "))
        
        if opc <= len(self.lista_filmes):
            print(f"Reproduzindo {self.lista_filmes[opc]}")
        else:
            print("Opção invalida!")

usu1 = Netflix("Celso", "@gmail", "12949021", "premium", "128437", "9534905", ["Harry Potter", "Vingadores", "Super Man", "Flash"])
print(usu1.nome)
print(usu1.plano)
Netflix.assistirFilme(usu1)