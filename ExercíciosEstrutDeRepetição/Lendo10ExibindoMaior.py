n1 = []
for i in range(10):
    num = int(input(f"Insira o {i + 1}° número: "))
    n1.append(num)

maior = max(n1)
print(f"O maior número é {maior}")
