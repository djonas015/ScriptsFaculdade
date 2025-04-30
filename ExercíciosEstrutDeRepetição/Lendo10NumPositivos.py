n = []
for i in range(10):
    num = int(input(f"Insira o {i + 1}° número: "))
    n.append(num)

positivos = [num for num in n if num >= 0]
print(*positivos)
