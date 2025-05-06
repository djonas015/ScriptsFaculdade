senha = 'W7@uz85Jo*'
while True:
    tentativas = input("Digite a senha: ")
    if tentativas == senha:
        print("Senha correta!")
        break
    else:
        print("Senha incorreta, tente novamente.")
