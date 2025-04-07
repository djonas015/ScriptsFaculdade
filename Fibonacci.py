n = int(input("Insira um número e veja a fórmula de Fibonacci: "))


def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia
    

print("A sequência de Fibonacci é: ")
print(fibonacci(n))
