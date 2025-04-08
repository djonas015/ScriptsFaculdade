numeros = []

print("Insira 10 números inteiros. \n"
      "Depois insira um número extra. \n"
      "Verificaremos quantas vezes o numero extra aparece na lista.")


for i in range(10):
    numero = int(input(f"Digite o {i + 1}° número inteiro: "))
    numeros.append(numero)

numeroadd = int(input("Digite o número extra: "))
contagem = numeros.count(numeroadd)
print(f"O número {numeroadd} aparece {contagem} vez(es) na lista")
