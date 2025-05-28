n = int(input("Insira N: "))


def fatorial(n):
    resultado = 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado


print(fatorial(n))
