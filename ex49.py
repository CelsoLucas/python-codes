n = int(input("Digite um numero: "))

t1 = 0
t2 = 1
print(f"{t1} -> {t2}", end="")
for f in range(n - 2):
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
print()