numeros = []

print("Insira 5 números interios e veja sua ordem inversa.")

for i in range(5):
    numero = int(input(f"Digite o {i + 1}° número inteiro: "))
    numeros.append(numero)

numeros.reverse()
print(f"A lista invertida é: {numeros}")
