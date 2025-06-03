def indice():
    lista = []
    for i in range(5):
        n = int(input(f"Insira o {i + 1}° número: "))
        lista.append(n)
    n1 = int(input("Deseja saber o indice de qual número? "))
    indice1 = lista.index(n1)
    print(f"O {n1} está na posição {indice1 + 1} da lista")


indice()
