import delorean

d1 = delorean.Delorean(timezone='America/Campo_Grande')
print("Data e hora atual em Campo Grande:", d1)


d3 = d1.shift('America/Sao_Paulo')
print("Data e hora em São Paulo:", d3)


if d1 > d3:
    print("Campo Grande está à frente de São Paulo.")
else:
    print("São Paulo está à frente de Campo Grande.")