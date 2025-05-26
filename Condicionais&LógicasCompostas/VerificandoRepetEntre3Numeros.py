n = []
for i in range(3):
    num = int(input(f"Insira {i + 1}° número: "))
    n.append(num)
if n[0] == n[1]:
    print("Há repetição dos números.")
elif n[1] == n[2]:
    print("Há repetição dos números.")
elif n[0] == n[2]:
    print("Há repetição dos números.")
else:
    print("Não tem repetição nos numeros")
