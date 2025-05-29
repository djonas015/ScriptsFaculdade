num = []


def maior_n():
    for i in range(3):
        n = int(input(f"Insira o {i + 1}° número: "))
        num.append(n)
    maior = max(num)
    return maior


print(maior_n())
