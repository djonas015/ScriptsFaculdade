lista = []
for i in range(5):
    n = int(input(f"Insira {i + 1}° número da lista: "))
    lista.append(n)

n1 = int(input("Insira um número e verificaremos se está na lista: "))
if n1 in lista:
    print(f"{n1} está na lista {lista}")
else:
    print(f"{n1} Não está na lista {lista}")
