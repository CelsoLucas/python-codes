import delorean


d1 = delorean.Delorean(timezone='America/Campo_Grande')
print("Data e hora atual em Campo Grande:", d1)

d3 = d1.shift('America/Sao_Paulo')
print("Data e hora em São Paulo:", d3)