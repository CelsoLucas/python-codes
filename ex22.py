qnt = float(input('Quantidade de maças: '))

if qnt < 12:
    preco = qnt * 0.30
    print('O valor total é:', preco)
else:
    preco = qnt * 0.25
    print('O valor total é:', preco)
