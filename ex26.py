n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))
media = (n1 + n2 + n3 + n4) / 4

if media >= 9.1:
    texto = "APROVADO"
    conc = "A"
elif media >= 7.6:
    texto = "APROVADO"
    conc = "B"
elif media >= 6:
    texto = "APROVADO"
    conc = "C"
elif media >= 4.1:
    texto = "REPROVADO"
    conc = "D"
elif media >= 0:
    texto = "REPROVADO"
    conc = "E"

print(f"Você foi {texto} pois seu conceito foi {conc}")

