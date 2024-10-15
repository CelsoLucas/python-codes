p1 = str(input("Telefonou para a vitima? ")).capitalize()
p2 = str(input("Esteve no local do crime? ")).capitalize()
p3 = str(input("Mora perto da vitima? ")).capitalize()
p4 = str(input("Devia para a vitima? ")).capitalize()
p5 = str(input("Ja trabalhou com a vitima? ")).capitalize()

cont = 0

if p1[0] == "S":
    cont += 1
if p2[0] == "S":
    cont += 1
if p3[0] == "S":
    cont += 1
if p4[0] == "S":
    cont += 1
if p5[0] == "S":
    cont += 1

if cont == 5:
    print("Assasino")
elif cont == 3 or cont ==4:
    print("Cumplice")
elif cont == 2:
    print("Suspeito")
elif cont <= 1:
    print("Inocente")