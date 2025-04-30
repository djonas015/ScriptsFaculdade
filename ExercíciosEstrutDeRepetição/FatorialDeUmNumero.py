n1 = int(input("Insira um número: "))
fatorial = 1

for i in range(1, n1 + 1):
    fatorial *= i
print(f"Fatorial de {n1} é {fatorial}")
