numero = int(input('Digite um número inteiro: '))

contador = 1
resultado = 1

while contador <= numero:
    resultado *= contador
    contador += 1

print(f"{numero}! = {resultado}")
