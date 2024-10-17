print("Morangos - Até 5kg R$2,50 por Kg - Acima de 5kg R$2,20 por Kg")
print("Maça - Até 5Kg R$1,80 por Kg - Acima de 5kg R$1,50 por Kg")

quant_mor = float(input("Digite quantos kilos de morango você deseja: "))
quant_maca = float(input("Digite quantos kilos de maça você deseja:"))

quant_tot = quant_maca + quant_mor

if quant_maca <= 5:
    valor_maca = quant_maca * 1.8
else:
    valor_maca = quant_maca * 1.5

if quant_mor <= 5:
    valor_mor = quant_mor * 2.5
else:
    valor_mor = quant_mor * 2.2

valor_tot = valor_mor + valor_maca

if quant_tot > 8 or valor_tot > 25:
    valor_tot = valor_tot - (valor_tot * 0.1)
    print(f"O valor total a pagar é de R${valor_tot}")
else:
    print(f"O valor total a pagar é de R${valor_tot}")