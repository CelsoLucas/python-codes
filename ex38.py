a = 80000
b = 200000
cont = 0
while a <= b:
    a += (a * 0.03)
    b += (b * 0.015)
    cont += 1

print(f"A: {a}")
print(f"B: {b}")
print(f"Para o A passar o B ele levou {cont} anos")
