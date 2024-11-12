import math
import datetime
import time
print("=-= Math =-=")
print(math.ceil(5.6))
print(math.floor(5.6))
print(math.fabs(-3))
print(math.factorial(5))
print(math.isqrt(81))
print(math.pow(2, 10))
print("=-= datetime =-=")
print(datetime.date.today())
print(datetime.date.today().strftime("%d/%m/%Y")) #para configurar o formato que quiser
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d/%m/%Y-%H-%M"))
print("=-= Time =-=")
a = 0
x = time.perf_counter()
while a < 10000:
    print(a)
    a += 1
y = time.perf_counter()
print(y - x)
