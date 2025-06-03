def potencia():
    import math
    n = int(input("Inisra a base: "))
    n1 = int(input("Insira expoente: "))
    pot = math.pow(n, n1)
    return pot


print(f"Resultado: {potencia()}")
