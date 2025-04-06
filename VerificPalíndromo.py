def palindromo(texto):
    texto = ''.join(reversed(texto))
    return texto


texto = input("Digite uma palavra ou frase e retornaremos se é um palíndromo ou não: ")
txt_invert = palindromo(texto)

if texto.replace(" ","").lower() == txt_invert.replace(" ", "").lower():
    print(f"'{texto}' é um palíndromo!")
else:
    print(f"'{texto}' Não é um palíndromo.")
