numeros = []

print("Digite 6 números inteiros, depois insira um número extra. \n"
      "Multiplicaremos o número extra por todos os 6 números inteiros.")

for i in range(6):
    n1 = int(input(f"Digite o {i + 1}° número inteiro: "))
    numeros.append(n1)

numero_extra = int(input("Digite o número extra: "))
multiplicacao = [numero_extra * n1 for n1 in numeros]
print(f"O valor do array multiplicado é:{multiplicacao} ")
