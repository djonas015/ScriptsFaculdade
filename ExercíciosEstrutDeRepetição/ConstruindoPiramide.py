n = int(input("Quantas linhas de pirâmide deseja? "))
for i in range(1, n + 1):
    espacos = ' ' * (n - i)
    aster = '*' * (2 * i - 1)
    print(espacos + aster)
