print("Insira 10 números interios. \n"
      "Calcularemos todos os números do Array")
numeros = []

for i in range(10):
    numero = int(input(f"Insira o {i + 1}° número inteiro "))
    numeros.append(numero)


def cl_soma(lista):
    return sum(lista)


resultado = cl_soma(numeros)
print(f"A soma de todos os números do array é: {resultado}")
