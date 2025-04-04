n1 = print("Insira 3 notas do aluno(a).")
notas = 0
for i in range(3):
    n1 = float(input(f"Insira a {i + 1}° nota do aluno: "))
    notas += n1

media = notas / 3
print(f"A média do aluno(a) é: {media:.2f}")
