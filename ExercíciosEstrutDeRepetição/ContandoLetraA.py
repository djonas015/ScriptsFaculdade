palavra = input("Insira uma palavra: ")
qtd = palavra.lower().count('a')

if qtd > 0:
    print(f"A palavra '{palavra}' possui {qtd} a`s")
else:
    print("Não possui a letra A na palavra inserida.")
