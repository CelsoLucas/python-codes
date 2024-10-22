cont_1 = 0
cont_2 = 0
cont_3 = 0
cont_4 = 0
cont_5 = 0
cont_6 = 0

while True:
    print("=-="*15)
    print("1 - Celso")
    print("2 - Anne")
    print("3 - Vitor")
    print("4 - Ederson")
    print('6 - Branco')
    print("Qualquer outro número - nulo")
    print("0 - Sair")
    opc = int(input("Digite o numero do canditado: "))

    if opc == 1:
        print("Voto Registrado!")
        cont_1 += 1
    elif opc == 2:
        print("Voto Registrado!")
        cont_2 += 1
    elif opc == 3:
        print("Voto Registrado!")
        cont_3 += 1
    elif opc == 4:
        print("Voto Registrado!")
        cont_4 += 1
    elif opc == 6:
        print("Voto Registrado!")
        cont_6 += 1

    elif opc == 0:
        break
    else:
        print("Voto Registrado!")
        cont_5 += 1
        
print("=-="*15)
print(f"Celso teve {cont_1} votos")
print(f"Anne teve {cont_2} votos")
print(f"Vitor teve {cont_3} votos")
print(f"Ederson teve {cont_4} votos")
print(f"{cont_6} Votos Brancos")
print(f"{cont_5} votos nulos")