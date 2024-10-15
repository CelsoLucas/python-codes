salario = float(input("Digite seu salário: "))

if salario <= 280:
    percentual = 20
    reajuste = salario + (salario * 0.2)
    diferenca = reajuste - salario
elif salario <= 700:
    percentual = 15
    reajuste = salario + (salario * 0.15)
    diferenca = reajuste - salario
elif salario <= 1500:
    percentual = 10
    reajuste = salario + (salario * 0.1)
    diferenca = reajuste - salario
elif salario > 1500:
    percentual = 5
    reajuste = salario + (salario * 0.05)
    diferenca = reajuste - salario

print(f"Seu salário antigo era de R${salario:.2f}")
print(f"O perncentual aplicado foi de {percentual}%")
print(f"O valor aumentado foi de R${diferenca:.2f}")
print(f"Seu novo salário é R${reajuste:.2f}")