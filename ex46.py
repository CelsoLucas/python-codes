n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
soma = 0
for n in range(n1+1, n2):
    soma += n
    print(n, end=" ")
print(f"\nA soma dos números resulta em {soma}")