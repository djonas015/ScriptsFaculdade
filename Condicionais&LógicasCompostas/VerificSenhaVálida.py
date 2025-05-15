senha = input("Insira a senha: ")
l1 = False
n1 = False

for letra in senha:
    if letra.isalpha():
        l1 = True
    elif letra.isdigit():
        n1 = True
if len(senha) >= 6:
    if l1 and n1:
        print(f"{senha} é uma senha válida.")
    else:
        print("Senha inválida")
else:
    print("Senha inválida")
