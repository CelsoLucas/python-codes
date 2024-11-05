while True:
    print("=-="*15)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("=-="*15)
    try:
        opc = int(input("Digite a Opção que deseja: "))

    except ValueError:
        print("=-="*15)
        print("Digite apenas números")
        continue

    while True:
        while True:
            try:
                print("=-="*15)
                n1 = float(input("N1: "))
                break
            except ValueError:
                print("=-="*15)
                print("Digite apenas números: ")
                continue
        while True:
            try:
                n2 = float(input("N2: "))
                break
            except ValueError:
                print("=-="*15)
                print("Digite apenas números: ")
                continue
        break
    print("=-="*15)

    if opc == 1:
        conta = n1 + n2
        print(f"{n1} + {n2} = {conta}")

    elif opc == 2:
        conta = n1 - n2
        print(f"{n1} - {n2} = {conta}")

    elif opc == 3:
        conta = n1 * n2
        print(f"{n1} * {n2} = {conta}")

    elif opc == 4:
        while True:
            try:
                conta = n1 / n2

            except ZeroDivisionError:
                print("Você não pode dividir um número por 0")
                try:
                    n2 = float(input("N2: "))
                except ValueError:
                    print("Digite apenas números: ")
                    continue
            else:
                print(f"{n1} / {n2} = {conta}")
                break
        
    else:
        print("Opção Invalida!")
            