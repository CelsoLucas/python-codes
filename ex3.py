real = float(input("Digite o valor que você tem em reais: R$"))
dolar = float(input("Digite o valor do dolar: $"))
conver = real / dolar
print(f"R${real} convertido para dolar é ${conver:.2f}")