a = 0
b = 1
n = 10


for i in range(n):
    print(a)
    prox = a + b
    a = b
    b = prox
