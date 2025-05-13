n1 = int(input("Insira um número: "))
n2 = int(input("Insira mais um número: "))
while n2 != 0:
    calculo = n1 % n2
    n1 = n2
    n2 = calculo
    if n2 == 0:
        print(n1)
        break
