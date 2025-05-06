qtd = int(input("Deseja Calcular a média de quantos números? "))
soma = 0
for i in range(qtd):
    n1 = int(input(f"Insira o {i + 1}° número: "))
    soma += n1

media = soma / qtd
print(media)
