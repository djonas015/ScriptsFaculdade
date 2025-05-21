p = input("Insira frase ou palavra: ").lower().replace('', ' ')
invert = p[::-1]
if invert == p:
    print("É um palíndromo")
else:
    print("Não é palíndromo")
