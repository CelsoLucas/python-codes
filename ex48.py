soma = 0
for c in range(1, 6):
    num = float(input(f"Número {c}: "))
    soma += num
med = soma / 5
print(f"A soma dos números é {soma} e a média das notas é {med}")