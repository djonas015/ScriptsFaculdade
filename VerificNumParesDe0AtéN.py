n = int(input("Insira um número: "))

for i in range(n):
    pares = [x for x in range(n) if x % 2 == 0]
    pares.append(n)


print(f"Os números pares de 0 até {n} são: {pares}")
