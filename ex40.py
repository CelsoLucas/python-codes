lista_produtos = []
total = 0
cont_nome = 0
cont_preco = 1
while True:
    print("=-="*15)
    nome = str(input("Nome: "))
    preco = float(input("Preço: R$")) 
    total += preco
    if nome == "0" and preco == 0:
        tamanho = int(len(lista_produtos) / 2)
        print("=-="*15)
        for c in range(0, tamanho):
            print(f"{lista_produtos[cont_nome]}  R${lista_produtos[cont_preco]}")
            cont_nome += 2
            cont_preco += 2
        print("=-="*15)
        print(f"Total a pagar: R${total}")
        while True:
            pagar = float(input("Pagar: R$"))
            if pagar < total:
                print("Valor invalido!")
                continue
            else:
                troco = pagar - total
                print(f"Seu troco será de R${troco}")
                cont_nome = 0
                cont_preco = 1
                lista_produtos.clear()
                total = 0
                break
    else:
        lista_produtos.append(nome)
        lista_produtos.append(preco)
