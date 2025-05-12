num = []
for i in range(5):
    nota = float(input(f"Insira a {i + 1}° nota: "))
    num.append(nota)

media = sum(num) / len(num)
print(f"A média é {media}")
