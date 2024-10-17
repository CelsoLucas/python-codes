print("File Duplo - Até 5kg R$5,80 por kg - Acima de 5kg R$4,90 por kg")
print("Alcatra - Até 5kg R$6,80 por kg - Acima de 5kg R$5,90 por kg")
print("Picanha - Até 5kg R$7,80 por kg - Acima de 5kg R$6,90 por kg")

lista = []
tipo = str(input("Digite qual carne você deseja: "))
quant = float(input("Digite a quantidade em kg que você deseja: "))

if tipo == "File Duplo":
    if quant <= 5:
        valor = quant * 5.8
    else:
        valor = quant * 4.9
elif tipo == "Alcatra":
    if quant <= 5:
        valor = quant * 6.8
    else:
        valor = quant * 5.9
elif tipo == "Picanha":
    if quant <= 5:
        valor = quant * 7.8
    else:
        valor = quant * 6.9
else:
    print("Corte não disponivel")

print("=-="*15)
print("Forma de Pagamento")
print("1 - Dinheiro ou Pix")
print("2 - Cartão Tabajara")
print("=-="*15)

pagamento = int(input("Digite a forma de pagamento: "))

if pagamento == 1:
    valor_tot = valor
    print("=-="*15)
    print("Cumpom Fiscal")
    print(f"Corte da carne: {tipo}")
    print(f"Quantidade: {quant}")
    print(f"Valor total R${valor_tot:.2f}")
    print(f"Valor do desconto R$00,00")
    print(f"Valor a pagar R${valor_tot:.2f}")

elif pagamento == 2:
    valor_tot = valor - (valor * 0.05)
    diferenca = valor - valor_tot
    print("=-="*15)
    print("Cumpom Fiscal")
    print(f"Corte da carne: {tipo}")
    print(f"Quantidade: {quant}")
    print(f"Valor total R${valor:.2f}")
    print(f"Valor do desconto R${diferenca:.2f}")
    print(f"Valor a pagar R${valor_tot:.2f}")