while True:
    print("=-="*15)
    print("CALCULADORA")
    print("=-="*15)
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opc = int(input("Digite a opção desejada: "))
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))

    print("=-="*15)
    
    if opc == 1:
        conta = n1 + n2
        print(f"{n1} + {n2} = {conta}")
    elif opc == 2:
        conta = n1 - n2
        print(f"{n1} - {n2} = {conta}")
    elif opc == 3:
        conta = n1 * n2
        print(f"{n1} X {n2} = {conta}")
    elif opc == 4:
        conta = n1 / n2
        print(f"{n1} / {n2} = {conta}")
    elif opc == 5:
        print("Saindo")
        break
    else:
        print("Opção invalida!")
