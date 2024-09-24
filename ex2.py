nome = str(input("Digite o nome do produto: "))
quant = int(input("Digite a quantidade: "))
valor = float(input("Digite o valor: R$"))
porc = int(input("Digite o percentual de desconto: "))

desc = (valor* quant) * (porc / 100)
tot = (valor*quant) - desc
print(f"O total a pagar do produto {nome} é R${tot}")