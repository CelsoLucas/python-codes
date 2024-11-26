import os
class Conta():
    def __init__(self, nome, saldo, cpf, senha):
        self.nome = nome
        self.__saldo = saldo
        self.__cpf = cpf
        self.__senha = senha

    def extrato(self, senha):
        if senha == self.__senha:
            print(f"Nome: {self.nome}")
            print(f"CPF: {self.__cpf}")
            print(f"Saldo: R${self.__saldo}")  
        else:
            print("Senha inválida")

    def depositar(self, valor_deposito):
        self.__saldo += valor_deposito
        print("Deposito efetuado com sucesso!")

    def sacar(self, senha, valor_saque):
        if senha == self.__senha:
            self.__saldo -= valor_saque
            print("Saque efetuado com sucesso!")

        else:
            print("Senha invalida!")

while True:
    os.system("cls")
    while True:
        print("1 - Cadastro")
        print("2 - Saldo")
        print("3 - Saque")
        print("4 - Depósito")
        try:
            opc = int(input("Opção: "))
        except ValueError:
            os.system("cls")
            print("Digte apenas números!")
            continue
        else:
            break
    if opc == 1:
        os.system("cls")
        print("=-="*15)
        print("Cadastro")
        print("=-="*15)
        while True:
            nome = str(input("Nome: "))
            if not nome.isalpha() and " " not in nome:
                print("Nome só pode ter letras")
                continue
            else:
                break
        
        while True:
            try:
                cpf = int(input("CPF (Apenas números): "))
            except ValueError:
                print("Digite apenas números")
                continue
            else:
                break
        
        senha = str(input("Senha: "))
        conta1 = Conta(nome, 0, cpf, senha)
        print("Cadastro realizado com sucesso!")
        os.system("pause")

    elif opc == 2:
        os.system("cls")
        senha = str(input("Digite sua senha: "))
        conta1.extrato(senha)
        os.system("pause")

    elif opc == 3:
        os.system("cls")
        senha = str(input("Digite sua senha: "))
        while True:
            try:
                valor = float(input("Valor do saque: R$"))
            except ValueError:
                print("Digite apenas números!")
                continue
            else:
                break
        conta1.sacar(senha, valor)
        os.system("pause")

    elif opc == 4:
        os.system("cls")
        while True:
            try:
                valor = float(input("Valor do deposito: R$"))
            except ValueError:
                print("Digite apenas números!")
                continue
            else:
                break
        conta1.depositar(valor)
        os.system("pause")
    else:
        os.system("cls")
        print("Opção invalida!")
        os.system("pause")