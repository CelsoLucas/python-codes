class Super():
    def __init__(self):
        self.nome = str(input("Digite seu nome: "))
        self.endereco = str(input("Digite seu endereço: "))
        self.cep = int(input("Digite seu cep: "))
        self.fone = int(input("Digite seu telefone: "))
        self.email = str(input("Digite seu email: "))
        self.data = str(input("Digite a data de nascimento: "))

class PessoaFisica(Super):
    def __init__(self):
        super().__init__()
        self.cpf = int(input("Digite seu cpf: "))
        self.rg = int(input("Digite seu rg: "))
        self.cnh = int(input("Digite sua cnh: "))

class PessoaJuridica(Super):
    def __init__(self):
        super().__init__()
        self.cnpj = int(input("Digite seu cnpj: "))
        self.rs = str(input("Digite a Razão Social: "))
        self.cnae = int(input("Digite cnae: "))
        self.end_comer = str(input("Digite o endereço comercial: "))
