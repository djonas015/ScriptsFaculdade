nummax = 100
nummin = 10
num = int(input("Insira um número: "))
if num <= nummax and num >= nummin:
    print(f"{num} está entre {nummin} e {nummax}")
else:
    print(f"{num} NÃO está entre {nummin} e {nummax}")
