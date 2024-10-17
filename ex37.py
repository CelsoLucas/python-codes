while True:
    while True:
        nome = str(input("Nome: "))
        if len(nome) <= 3:
            print("Nome deve ter mais de 3 caracteres!")
        else:
            break
    while True:
        idade = int(input("Idade: "))
        if idade < 0 or idade > 150:
            print("Idade deve estar entre 0 e 150!")
        else:
            break
    while True:
        salario = float(input("Salário: R$"))
        if salario < 0:
            print("Salario deve ser maior que R$00,00")
        else:
            break
    while True:
        sexo = str(input("Sexo: ")).upper()
        lista_sexo = ["F", "M", "O"]
        if sexo not in lista_sexo:
            print(f"Sexo deve estar entre esses: {lista_sexo}")
        else:
            break
    while True:
        estado = str(input("Estado Civil: ")).upper()
        lista_estado = ["S", "C", "V", "D"]
        if estado not in lista_estado:
            print(f"Estado Civil deve estar entre esses: {lista_estado}")
        else:
            break
    break
