while True:
    nota = int(input("Digite uma nota: "))
    if nota >= 0 and nota <= 10:
        print("Valor valido!")
        break
    else:
        print("Valor Invalido! Tente Novamente")