def fatorial():
    n = int(input("Insira um número: "))
    resultado = 1
    for i in range(n, 1, -1):
        resultado *= i
    return resultado


print(fatorial())
