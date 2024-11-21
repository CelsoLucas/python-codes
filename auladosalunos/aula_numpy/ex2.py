import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
par = []
soma = 0
cont = 0
for i in array:
    if i % 2 == 0:
        print(i)
    else:
        soma += i
        cont += 1
med = soma / cont
print(med)