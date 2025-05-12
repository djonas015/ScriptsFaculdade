num = []
for i in range(10):
    n1 = int(input(f"Insira o {i + 1}° número: "))
    num.append(n1)

menor = min(num)
print(f"O menor número é {menor}")
