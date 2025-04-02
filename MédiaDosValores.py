numeros = []

print("Digite 6 números inteiros para obter a média dos valores.")
for i in range(6):
    numero = int(input(f"Digite o {i + 1}° número inteiro: "))
    numeros.append(numero)
    media = sum(numeros) / len(numeros)

print(f"A média dos valores digitados é: {media:.2f}")
