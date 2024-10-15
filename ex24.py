n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4
if media == 10:
    print(f"Sua média foi {media} Aprovado com distinção")
elif media >= 7:
    print(f"Sua média foi {media} Você foi aprovado!")
else:
    print(f"Sua média foi {media} Você foi reprovado!")
