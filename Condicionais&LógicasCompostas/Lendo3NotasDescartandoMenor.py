n1 = []
for i in range(3):
    n2 = int(input(f"Insira a {i + 1}° nota: "))
    n1.append(n2)
menor = min(n1)
n1.remove(menor)
print(n1)
