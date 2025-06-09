def contando_vogais():
    contador = 0
    frase = input("Insira uma frase: ").lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    for letra in frase:
        if letra in vogais:
            contador += 1
    if contador > 0:
        print(f"A frase possui {contador} vogais")
    else:
        print("Não possui vogais na frase!")


contando_vogais()
