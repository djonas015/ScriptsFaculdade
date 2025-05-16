num = []
for i in range(3):
    n1 = int(input(f"Insira o {i + 1}° número: "))
    num.append(n1)

maior = max(num)
print(f"{maior} é o maior número dos 3")
