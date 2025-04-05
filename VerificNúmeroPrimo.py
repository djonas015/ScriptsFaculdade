import math


def verificacao(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:

        for i in range(2, int(math.sqrt(numero) + 1)):
            if numero % i == 0:
                return False
        return True
    

numero = int(input("Insira o número para verificar se é primo: "))
if verificacao(numero):
    print(f"O {numero} é um número primo!")
else:
    print(f"O {numero} não é um número primo.")
