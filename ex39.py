a = float(input("População A: "))
taxaa = float(input("Taxa A: "))

b = float(input("População B: "))
taxab = float(input("Taxa B: "))

cont = 0
while a <= b:
    a += (a * (taxaa / 100))
    b += (b * (taxab / 100))
    cont += 1

print(f"A: {a}")
print(f"B: {b}")
print(f"Para o A passar o B ele levou {cont} anos")
