n = int(input("Digite um numero: "))

t1 = 0
t2 = 1
c = 2
print(f"{t1} -> {t2}", end="")
for f in range(n - c):
    t3 = t1 + t2
    print(f" -> {t3}", end="")
    t1 = t2
    t2 = t3
    c += 1
print()