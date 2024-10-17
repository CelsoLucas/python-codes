while True:
    usu = str(input("Usuario: "))
    senha = str(input("Senha: "))
    if senha == usu:
        print("Senha não pode ser igual ao usuario!")
    else:
        print("Bem Vindo!")
        break
