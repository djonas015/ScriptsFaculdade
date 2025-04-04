list = []

print("Insira 5 números inteiros. Retornaremos em ordem crescente.")
for i in range(5):
    n1 = int(input(f"Insira o {i + 1}° número inteiro: "))
    list.append(n1)

ordem = sorted(list)
print(f"Esses são os números inseridos em ordem crescente: {ordem}")
