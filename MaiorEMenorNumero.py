numeros = []

for i in range(8):
    numero = int(input(f"Insira o {i + 1}° número inteiro "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)
print(f"O maior número inserido foi {maior}")
print(f"O menor número inserido foi {menor}")
