num = int(input("Insira um número: "))
n1 = 0
for i in range(1, num):
    if num % i == 0:
        n1 += i
if n1 == num:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} não é um número perfeito")
