n = int(input("Quantos número você deseja inserir? "))
for i in range(n):
    verif = int(input(f"Insira o {i + 1} número: "))

    if verif == 0:
        print("Programa encerrado")
        break
