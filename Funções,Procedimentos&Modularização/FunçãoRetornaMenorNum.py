def menor_num():
    lista = []
    for i in range(5):
        n = int(input(f"Insira o {i + 1}° número: "))
        lista.append(n)
    menor = min(lista)
    print(f"Menor número da lista: {menor}")


menor_num()
