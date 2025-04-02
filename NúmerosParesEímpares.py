numeros = []

print("Digite 10 números inteiros e exibiremos somente os pares.")

for i in range(10):
    numero = int(input(f"Digite o {i + 1}° número inteiro: "))
    numeros.append(numero)

pares = [x for x in numeros if x % 2 == 0]
print(f"Os números pares digitados foram:{pares}")
