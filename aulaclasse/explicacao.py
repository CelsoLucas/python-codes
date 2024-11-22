# class Vendedor():
#     def __init__(self, nome, vendas):
#         self.nome = nome
#         self.vendas = vendas
#     def vendeu(self, vendas):
#         self.vendas = vendas
#         print(self.vendas)
#     def bateu_meta(self, meta):
#         if self.vendas >= meta:
#             return "Bateu a meta"
#         else:
#             return "Não bateu a meta"
# vendedor1 = Vendedor("Celso", 1000)
# print(vendedor1.bateu_meta(100))

class Controleremoto():
    def __init__(self, cor, profundidade, largura):
        self.cor = cor
        self.profundidade = profundidade
        self.largura = largura

    def mudar_canal(self, botao):
        if botao == "+":
            print("Aumentando Volume")
        elif botao == "-":
            print("Diminuindo Volume")
        else:
            print("Valor Invalido")
    def desligar_ligar(self, botao):
        if botao == 0:
            print("Desligando")
        elif botao == 1:
            print("Ligando")
        else:
            print("Botao invalido")

print()
while True:
    print("1 - Controle da Sala")
    print("2 - Controle do Quarto 1")
    print("3 - Controle do Quarto 2")
    print("4 - Controle do Quarto 3")
    print("5 - Controle do Quarto 5")
    
    opc = int(input("Qual você deseja: "))

    if opc == 1:
        controle1 = Controleremoto("Preto", "1cm", "1cm")
        print(controle1.cor, controle1.profundidade, controle1.largura)
        while True:
            print("0 - Desligar/Ligar")
            print("1 - Aumentar/Diminuir Volume")
            opc = int(input("Digite a opção: "))
            if opc == 0:
                while True:
                    botao_ligar = int(input("0 para desligar 1 para ligar"))
                    if botao_ligar == 10:
                        break
                    else:
                        ligar = controle1.desligar_ligar(botao_ligar)
            elif opc == 1:
                while True:
                    btn1 = str(input("+ para aumentar - para diminuir volume "))
                    if btn1 == "+-":
                        break
                    else:
                        volume = controle1.mudar_canal(btn1)
            else:
                break

    elif opc == 2:
        controle2 = Controleremoto("Cinza", "1.5cm", "0.8cm")
        print(controle2.cor, controle2.profundidade, controle2.largura)
        while True:
            print("0 - Desligar/Ligar")
            print("1 - Aumentar/Diminuir Volume")
            opc = int(input("Digite a opção: "))
            if opc == 0:
                while True:
                    botao_ligar = int(input("0 para desligar 1 para ligar"))
                    if botao_ligar == 10:
                        break
                    else:
                        ligar = controle2.desligar_ligar(botao_ligar)
            elif opc == 1:
                while True:
                    btn1 = str(input("+ para aumentar - para diminuir volume "))
                    if btn1 == "+-":
                        break
                    else:
                        volume = controle2.mudar_canal(btn1)
            else:
                break

    elif opc == 3:
        controle3 = Controleremoto("Branca", "1.2cm", "0.9cm")
        print(controle3.cor, controle3.profundidade, controle3.largura)
        while True:
            print("0 - Desligar/Ligar")
            print("1 - Aumentar/Diminuir Volume")
            opc = int(input("Digite a opção: "))
            if opc == 0:
                while True:
                    botao_ligar = int(input("0 para desligar 1 para ligar"))
                    if botao_ligar == 10:
                        break
                    else:
                        ligar = controle3.desligar_ligar(botao_ligar)
            elif opc == 1:
                while True:
                    btn1 = str(input("+ para aumentar - para diminuir volume "))
                    if btn1 == "+-":
                        break
                    else:
                        volume = controle3.mudar_canal(btn1)
            else:
                break

    elif opc == 4:
        controle4 = Controleremoto("Preto", "1cm", "1.2cm")
        print(controle4.cor, controle4.profundidade, controle4.largura)
        while True:
            print("0 - Desligar/Ligar")
            print("1 - Aumentar/Diminuir Volume")
            opc = int(input("Digite a opção: "))
            if opc == 0:
                while True:
                    botao_ligar = int(input("0 para desligar 1 para ligar"))
                    if botao_ligar == 10:
                        break
                    else:
                        ligar = controle4.desligar_ligar(botao_ligar)
            elif opc == 1:
                while True:
                    btn1 = str(input("+ para aumentar - para diminuir volume "))
                    if btn1 == "+-":
                        break
                    else:
                        volume = controle4.mudar_canal(btn1)
            else:
                break

    elif opc == 5:
        controle5 = Controleremoto("Preto", "0.9cm", "1cm")
        print(controle5.cor, controle5.profundidade, controle5.largura)
        while True:
            print("0 - Desligar/Ligar")
            print("1 - Aumentar/Diminuir Volume")
            opc = int(input("Digite a opção: "))
            if opc == 0:
                while True:
                    botao_ligar = int(input("0 para desligar 1 para ligar"))
                    if botao_ligar == 10:
                        break
                    else:
                        ligar = controle5.desligar_ligar(botao_ligar)
            elif opc == 1:
                while True:
                    btn1 = str(input("+ para aumentar - para diminuir volume "))
                    if btn1 == "+-":
                        break
                    else:
                        volume = controle5.mudar_canal(btn1)
            else:
                break
    else:
        break