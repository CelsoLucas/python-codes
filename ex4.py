nome = str(input("Digite o nome: "))
idade = int(input("Digite a idade: "))
sexo = str(input("Digite o sexo (M/F): "))
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2) / 2

print(f"{nome} tem {idade} anos e é do sexo {sexo}, tirou na primeira prova {n1} e na segunda {n2} e está com a média {media}")
