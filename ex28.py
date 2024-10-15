print("G - Gasolina R$2,50/L")
print("A - Álcool R$1,90/L")
comb = str(input("Digite qual você deseja: "))
litros = float(input("Digite quantos litros você deseja: "))

if comb == "G":
    if litros <= 20:
        valor = 2.5 * litros
        desc = valor * 0.03
        valor_tot = valor - desc
        print(f"O valor total será de R${valor_tot:.2f}")
    else:
        valor = 2.5 * litros
        desc = valor * 0.05
        valor_tot = valor - desc
        print(f"O valor total será de R${valor_tot:.2f}")

elif comb == "A":
    if litros <= 20:
        valor = 1.9 * litros
        desc = valor * 0.04
        valor_tot = valor - desc
        print(f"O valor total será de R${valor_tot:.2f}")
    else:
        valor = 1.9 * litros
        desc = valor * 0.06
        valor_tot = valor - desc
        print(f"O valor total será de R${valor_tot:.2f}")