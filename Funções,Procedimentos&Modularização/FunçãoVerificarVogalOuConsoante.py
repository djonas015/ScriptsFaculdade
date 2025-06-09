def verificar_letra():
    letra = input("Insira uma letra: ").lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra in vogais:
        print("É vogal")
    else:
        print("É consoante!")


verificar_letra()
